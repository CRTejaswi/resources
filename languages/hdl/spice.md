    Copyright(c) 2021-
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+

# SPICE
> Info

# Index

- 
- 
- 

# Diode Characteristics
# Transistor Characteristics

```spice
// JFET: Drain Characteristics
vGS 1 0 0V
vDS 2 0 0V
J 2 1 0 NJFET
.MODEL NJFET NJF (Vto=-4V Beta=0.0005ApVsg + Rd=1ohm Rs=1ohm CGS=2pF CGD=2pF)
.DC vDS 0V 25V 0.5V vGS 0V -4V 0.5V
.PROBE
.END

// JFET: Transfer Characteristics
vGS 1 0 0V
vDS 2 0 0V
J 2 1 0 NJFET
.MODEL NJFET NJF (Vto=-4V Beta=0.0005ApVsg + Rd=1ohm Rs=1ohm CGS=2pF CGD=2pF)
.DC vGS 0V -4V 0.5V
.PROBE
.END

// MOSFET: Drain Characteristics
vGS 1 0 0V
vDS 2 0 0V
M 2 1 0 0 NMOSG
.MODEL NMOSG NMOS (Vto=4V Kp=0.0008ApVsq + Rd=1ohm Rg=1kohm)
.DC vDS 0V 25V 0.5V vGS 0V 8V 1V
.PROBE
.END

// MOSFET: Transfer Characteristics
vGS 1 0 0V
vDS 2 0 0V
M 2 1 0 0 NMOSG
.MODEL NMOSG NMOS (Vto=4V Kp=0.0008ApVsq + Rd=1ohm Rg=1kohm)
.DC vGS 0V 8V 0.1V
.PROBE
.END
```

# References

