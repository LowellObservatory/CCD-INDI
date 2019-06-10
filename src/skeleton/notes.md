## Writing a DTD specified XML skeleton file.

Elwood's document defines things like:
```XML
<!ENTITY % numberValue "(#PCDATA)" >
```
and uses this ENTITY both in ATTLIST definitions as well as for ELEMENT definitions.

In a DTD, this doesn't work for both, I had to define it this way:
```XML
<!ENTITY % numberFormat  "CDATA" >
```
to make it work in the ATTLIST.  Later, I found that the above ENTITY definition did
not work in an ELEMENT definition so I made a new ELEMENT called "Number":
```XML
<!ELEMENT Number (#PCDATA)>
```
for use in the definition of "defNumber":
```XML
<!ELEMENT defNumber (Number) >
```

Also, Elwood defines some entities with choices like this:
```XML
<!ENTITY % propertyState "(Idle|Ok|Busy|Alert)" >
```
but never defines any ELEMENTS for "Idle, Ok, Busy, Alert".
To make this work these must be defined in the DTD:
```XML
<!ELEMENT Idle EMPTY>
<!ELEMENT Ok EMPTY>
<!ELEMENT Busy EMPTY>
<!ELEMENT Alert EMPTY>
```
This is used in the XML file like this:
```XML
<defLightVector device="Test Device" name="Light Property" label=""
    group="Main Control" state="Idle">
    <defLight name="Light 1" label="L1">
        <Idle/>
    </defLight>
    <defLight name="Light 2" label="L2">
        <Idle/>
    </defLight>
    <defLight name="Light 3" label="L3">
        <Idle/>
    </defLight>
    <defLight name="Light 4" label="L4">
        <Idle/>
    </defLight>
    <defLight name="Light 5" label="L5">
        <Idle/>
    </defLight>
</defLightVector>
```
which differs from the example XML skeleton file I found on the internet:
```XML
<defLightVector device="Test Device" name="Light Property" label=""
    group="Main Control" state="Idle">
    <defLight name="Light 1" label="L1">
        Idle
    </defLight>
    <defLight name="Light 2" label="L2">
        Idle
    </defLight>
    <defLight name="Light 3" label="L3">
        Idle
    </defLight>
    <defLight name="Light 4" label="L4">
        Idle
    </defLight>
    <defLight name="Light 5" label="L5">
        Idle
    </defLight>
</defLightVector>
```
Note the use of text in the second example and tags in the first example.
