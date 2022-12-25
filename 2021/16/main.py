from utils import *


class BitsFeeder:
    def __init__(self, hex_string):
        self.current_byte = None
        self.hex_string = hex_string
        self.index = 0
        self.bitpos = 0

    def get_bit(self):
        if self.bitpos == 0:
            self.current_byte = int(self.hex_string[self.index:self.index + 2], 16)
            self.index += 2
            self.bitpos = 8
        self.bitpos -= 1
        return (self.current_byte >> self.bitpos) & 1

    def get_bits(self, count):
        result = 0
        for i in range(count):
            result <<= 1
            result |= self.get_bit()
        return result

    def pad(self):
        while self.bitpos != 0:
            self.get_bit()

    def position(self):
        return self.index * 4 - self.bitpos

    def __bool__(self):
        return self.index < len(self.hex_string) or self.bitpos != 0


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip()


class Packet:
    def __init__(self, version, packet_type):
        self.version = version
        self.packet_type = packet_type

    def versions(self):
        yield self.version


class ValuePacket(Packet):
    def __init__(self, version, packet_type, value):
        super().__init__(version, packet_type)
        self.value = value

    def calc(self):
        return self.value


operators = {
    0: lambda values: sum(values),
    1: lambda values: mul(values),
    2: lambda values: min(values),
    3: lambda values: max(values),
    5: lambda values: 1 if values[0] > values[1] else 0,
    6: lambda values: 1 if values[0] < values[1] else 0,
    7: lambda values: 1 if values[0] == values[1] else 0,
}


class OperatorPacket(Packet):
    def __init__(self, version, packet_type, sub_packets):
        super().__init__(version, packet_type)
        self.sub_packets = sub_packets

    def versions(self):
        yield from super().versions()
        for sub_packet in self.sub_packets:
            yield from sub_packet.versions()

    def calc(self):
        values = [sub_packet.calc() for sub_packet in self.sub_packets]
        return operators[self.packet_type](values)


def parse_packet(feeder):
    version = feeder.get_bits(3)
    packet_type = feeder.get_bits(3)
    if packet_type == 4:
        value = 0
        while True:
            end_bit = feeder.get_bit()
            value <<= 4
            value |= feeder.get_bits(4)
            if end_bit == 0:
                break
        return ValuePacket(version, packet_type, value)
    else:
        i = feeder.get_bit()
        sub_packets = []
        if i == 0:
            length = feeder.get_bits(15)
            start = feeder.position()
            while feeder.position() - start < length:
                packet = parse_packet(feeder)
                sub_packets.append(packet)
        else:
            count = feeder.get_bits(11)
            for _ in range(count):
                packet = parse_packet(feeder)
                sub_packets.append(packet)
        return OperatorPacket(version, packet_type, sub_packets)


def packet_from_string(string):
    feeder = BitsFeeder(string)
    packet = parse_packet(feeder)
    feeder.pad()
    return packet


def task1(filename):
    data = read_data(filename)
    versions = []
    packet = packet_from_string(data)
    versions.extend(packet.versions())
    return sum(versions)


def task2(filename):
    data = read_data(filename)
    packet = packet_from_string(data)
    return packet.calc()


assert list(packet_from_string('D2FE28').versions()) == [6]
assert list(packet_from_string('38006F45291200').versions()) == [1, 6, 2]
assert list(packet_from_string('EE00D40C823060').versions()) == [7, 2, 4, 1]
assert list(packet_from_string('8A004A801A8002F478').versions()) == [4, 1, 5, 6]
assert list(packet_from_string('620080001611562C8802118E34').versions()) == [3, 0, 0, 5, 1, 0, 3]
assert list(packet_from_string('C0015000016115A2E0802F182340').versions()) == [6, 0, 0, 6, 4, 7, 0]
assert list(packet_from_string('A0016C880162017C3686B18A3D4780').versions()) == [5, 1, 3, 7, 6, 5, 2, 2]

assert packet_from_string('D2FE28').calc() == 2021
assert packet_from_string('38006F45291200').calc() == 1
assert packet_from_string('EE00D40C823060').calc() == 3
assert packet_from_string('8A004A801A8002F478').calc() == 15
assert packet_from_string('620080001611562C8802118E34').calc() == 46
assert packet_from_string('C0015000016115A2E0802F182340').calc() == 46
assert packet_from_string('A0016C880162017C3686B18A3D4780').calc() == 54

assert task1('data.txt') == 949
assert task2('data.txt') == 1114600142730
