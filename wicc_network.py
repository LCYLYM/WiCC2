#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    WiCC (Wifi Cracking Camp)
    Second version of the original WiCC tool at https://github.com/pabloibiza/WiCC
    GUI tool for wireless pentesting on WEP and WPA/WPA2 networks.
    Project developed by Pablo Sanz Alguacil, Miguel Yanes Fernández.
"""


class Network:
    id = ""
    bssid = ""
    first_seen = ""
    last_seen = ""
    channel = 0
    speed = 0
    privacy = ""
    cipher = ""
    authentication = ""
    power = 0
    beacons = 0
    ivs = 0
    lan_ip = ""
    essid = ""
    handshake = False
    password = ""
    num_clients = 0
    clients = []

    def __init__(self, id, bssid, first_seen, last_seen, channel, speed, privacy, cipher, authentication, power,
                 beacons, ivs, lan_ip, essid, handshake, password, num_clients):
        """
        Constructor for the Network class
        :param id: string. Id of the network
        :param bssid: string. Address of the network
        :param first_seen: date. Date when the network was seen the first time
        :param last_seen: date. Date when the network was seen the last time
        :param channel: int. Channel where the network is working on
        :param speed: int. Speed of the connection
        :param privacy: string. Type of privacy being used. EX: WPA, WPA2, WEP
        :param cipher: string. Type of cipher. EX: CCMP
        :param authentication: string. Type of authentication. EX: PSK
        :param power: int. Power of the network
        :param beacons: int. Number of beacons detected on the network
        :param ivs: int. Number of IV's
        :param lan_ip: string. **not really sure what this is**
        :param essid: string. Name of the network (in case it has one)
        :param handshake: boolean. Boolean if a handshake has been captured in the network
        :param password: boolean. Boolean if the password has been cracked for the network
        :param clients: number of connected clients on the network
        """
        self.id = id
        self.bssid = bssid
        self.first_seen = first_seen
        self.last_seen = last_seen
        self.channel = channel
        self.speed = speed
        self.privacy = privacy
        self.cipher = cipher
        self.authentication = authentication
        self.power = power
        self.beacons = beacons
        self.ivs = ivs
        self.lan_ip = lan_ip
        self.essid = essid
        self.handshake = handshake
        self.password = password
        self.num_clients = num_clients
        self.clients = []

    def __str__(self):
        """
        Creates a string with the class parameters
        :return: string of parameters
        """
        output = ""
        output.__add__("ID: " + str(self.id))
        output.__add__(" BSSID: " + self.bssid)
        output.__add__(" First Seen: " + self.first_seen)
        output.__add__(" Last Seen: " + self.last_seen)
        output.__add__(" Channel: " + str(self.channel))
        output.__add__(" Speed: " + str(self.speed))
        output.__add__(" Privacy: " + self.privacy)
        output.__add__(" Cipher:" + self.cipher)
        output.__add__(" Authentication: " + self.authentication)
        output.__add__(" Power: " + str(self.power))
        output.__add__(" Beacons: " + str(self.beacons))
        output.__add__(" IVs: " + str(self.ivs))
        output.__add__(" LAN-IP: " + self.lan_ip)
        output.__add__(" ESSID: " + self.essid)
        output.__add__(" Handshake: " + str(self.handshake))
        output.__add__(" Password: " + self.password)
        output.__add__(" Clients: " + str(self.clients))
        return output

    def get_list(self):
        """
        Generates a list with the class parameters
        :return: list of parameters (will be used by the view to print the networks)
        """
        list = []
        list.append(self.id)
        list.append(self.bssid)
        list.append(self.first_seen)
        list.append(self.last_seen)
        list.append(self.channel)
        list.append(self.speed)
        list.append(self.privacy)
        list.append(self.cipher)
        list.append(self.authentication)
        list.append(self.power)
        list.append(self.beacons)
        list.append(self.ivs)
        list.append(self.lan_ip)
        list.append(self.essid)
        list.append(self.handshake)
        list.append(self.password)
        list.append(self.num_clients)
        list.append(self.clients)
        return list

    def add_client(self, client):
        """
        Sum 1 to the number of connected clients on the network
        :return:
        """
        self.clients.append(client)
        self.num_clients += 1

    def get_first_client(self):
        if self.clients:
            return self.clients[0]

    def get_bssid(self):
        return self.bssid

    def get_essid(self):
        return self.essid

    def get_channel(self):
        return self.channel

    def get_encryption(self):
        return self.privacy

    def get_id(self):
        return self.id

    def get_clients(self):
        return self.num_clients

