# A pyang plugin to produce a JSON representation of module trees for use in graph libraries

This simplistic pyang plugin produces a JSON representation from YANG files. The output can be fed through a variety of libraries for data visualization. Development is mainly done for use with [D3](https://d3js.org/), e.g. using [Hierarchies (d3-hierarchy)](https://github.com/d3/d3/blob/master/API.md#hierarchies-d3-hierarchy).

Some libraries require certain objects, e.g. D3 expects `name` and `children` objects for structure. This may need to be adjusted in the plugin code for other libraries. Should likely be moved to options.

## Example
```
$ pyang -f jsontree ietf-interfaces\@2014-05-08.yang
{
  "contact": "WG Web:   <http://tools.ietf.org/wg/netmod/>\nWG List:  <mailto:netmod@ietf.org>\n\nWG Chair: Thomas Nadeau\n          <mailto:tnadeau@lucidvision.com>\n\nWG Chair: Juergen Schoenwaelder\n          <mailto:j.schoenwaelder@jacobs-university.de>\n\nEditor:   Martin Bjorklund\n          <mailto:mbj@tail-f.com>",
  "name": "ietf-interfaces",
  "organization": "IETF NETMOD (NETCONF Data Modeling Language) Working Group",
  "type": "module",
  "children": [
    {
      "description": "Interface configuration parameters.",
      "type": "container",
      "name": "interfaces",
      "children": [
        {
          "description": "The list of configured interfaces on the device.\n\nThe operational state of an interface is available in the\n/interfaces-state/interface list.  If the configuration of a\nsystem-controlled interface cannot be used by the system\n(e.g., the interface hardware present does not match the\ninterface type), then the configuration is not applied to\nthe system-controlled interface shown in the\n/interfaces-state/interface list.  If the configuration\nof a user-controlled interface cannot be used by the system,\nthe configured interface is not instantiated in the\n/interfaces-state/interface list.",
          "type": "list",
          "name": "interface",
          "children": [
            {
              "description": "The name of the interface.\n\nA device MAY restrict the allowed values for this leaf,\npossibly depending on the type of the interface.\nFor system-controlled interfaces, this leaf is the\ndevice-specific name of the interface.  The 'config false'\nlist /interfaces-state/interface contains the currently\nexisting interfaces on the device.\n\nIf a client tries to create configuration for a\nsystem-controlled interface that is not present in the\n/interfaces-state/interface list, the server MAY reject\nthe request if the implementation does not support\npre-provisioning of interfaces or if the name refers to\nan interface that can never exist in the system.  A\nNETCONF server MUST reply with an rpc-error with the\nerror-tag 'invalid-value' in this case.\n\nIf the device supports pre-provisioning of interface\nconfiguration, the 'pre-provisioning' feature is\nadvertised.\n\nIf the device allows arbitrarily named user-controlled\ninterfaces, the 'arbitrary-names' feature is advertised.\n\nWhen a configured user-controlled interface is created by\nthe system, it is instantiated with the same name in the\n/interface-state/interface list.",
              "type": "leaf",
              "name": "name",
              "children": []
            }
          ]
        }
      ]
    }
   [...]
  ]
}
```