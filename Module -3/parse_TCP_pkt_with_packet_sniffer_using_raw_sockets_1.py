# The length of TCP header always lies in the range- [20 bytes , 60 bytes]
# Minimum length of TCP header = 5 x 4 bytes = 20 bytes.
# Maximum length of TCP header = 20 bytes + 40 bytes = 60 bytes.

# https://www.freesoft.org/CIE/Course/Section4/8.htm

#                     TCP Header Format

                                    
#    0                   1                   2                   3   
#    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 
#  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#   |          Source Port          |       Destination Port        |
#  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#   |                        Sequence Number                        |
#  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#   |                    Acknowledgment Number                      |
#   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#   |  Data |           |U|A|P|R|S|F|                               |
#   | Offset| Reserved  |R|C|S|S|Y|I|            Window             |
#   |       |           |G|K|H|T|N|N|                               |
#   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#   |           Checksum            |         Urgent Pointer        |
#   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#   |                    Options                    |    Padding    |
#   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#   |                             data                              |
#   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
#                           TCP Header Format

#          Note that one tick mark represents one bit position.



# Source Port: 16 bits
# Destination Port: 16 bits
# Sequence Number: 32 bits
# Acknowledgment Number: 32 bits
# Data Offset: 4 bits
# Reserved: 6 bits
# Control Bits: 6 bits (from left to right):

#    URG:  Urgent Pointer field significant
#   ACK:  Acknowledgment field significant
#    PSH:  Push Function
#    RST:  Reset the connection
#    SYN:  Synchronize sequence numbers
#    FIN:  No more data from sender

# Window: 16 bits
# Checksum: 16 bits
#Urgent Pointer: 16 bits
#Options: variable
#Padding: variable



