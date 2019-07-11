""" Define constants and data structures used for INDI Property Definitions.
    Based on the indiapi.h definitions (version 1.7) by Elwood C. Downey.
"""

from enum import Enum

# Switch state.
ISState = Enum('ISState', 'ISS_OFF ISS_ON')

# Property State.
IPState = Enum('IPState', 'ISP_IDLE ISP_OK IPS_BUSY IPS_ALERT')

# Switch vector rule hint.
# ISR_1OFMANY: Only 1 switch of many can be ON (e.g. radio buttons)
# ISR_ATMOST1: At most one switch can be ON, but all switches can be off.
#     Similar to ISR_1OFMANY with the exception that all switches can be off.
# ISR_NOFMANY: Any number of switches can be ON (e.g. check boxes)
ISRule = Enum('ISRule', 'ISR_1OFMANY ISR_ATMOST1 ISR_NOFMANY')

# Permission hint, with respect to client.
# RO: Read Only
# WO: Write Only
# RW: Read & Write
IPerm = Enum('IPerm', 'IP_RO IP_WO IP_RW')

# IText structure
# One text descriptor.
class IText():
    def __init__(self, name, label, text, tvp, aux0, aux1):
        self.name  = name   # Index Name  (string)
        self.label = label  # Short Description (string)
        self.text  = text   # Allocated text string (string)
        self.tvp   = tvp    # Pointer to Parent (ITextVectorProperty)
        self.aux0  = aux0   # Helper info (None)
        self.aux1  = aux1   # Helper info (None)

# ITextVectorProperty structure
# Text vector property descriptor.
class ITextVectorProperty():
    def __init__(self, device, name, label, group, p, timeout, s, tp,
        ntp, timestamp, aux):
        self.device = device        # Device name (string)
        self.name = name            # Property name (string)
        self.label = label          # Short description (string)
        self.group = group          # GUI grouping hint (string)
        self.p = p                  # Client sccessibility hint (IPerm)
        self.timeout = timeout      # Current max time to change, secs (double)
        self.s = s                  # Current property state (IPState)
        self.tp = tp                # Texts comprising this vector (IText[])
        self.ntp = ntp              # Dimension of tp[] (int)
        self.timestamp = timestamp  # ISO 8601 timestamp of this event (string)
        self.aux = aux              # Helper info (None)