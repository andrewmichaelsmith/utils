#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#
# Generated Tue Nov 06 14:02:41 2012 by generateDS.py version 2.7c.
#

import sys
import getopt
import re as re_

import cybox_common_types_1_0

etree_ = None
Verbose_import_ = False
(   XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
    ) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError("Failed to import ElementTree from any known place")

def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
        'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# User methods
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ImportError, exp:

    class GeneratedsSuper(object):
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_validate_integer(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_integer_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of integers')
            return input_data
        def gds_format_float(self, input_data, input_name=''):
            return '%f' % input_data
        def gds_validate_float(self, input_data, node, input_name=''):
            return input_data
        def gds_format_float_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_float_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of floats')
            return input_data
        def gds_format_double(self, input_data, input_name=''):
            return '%e' % input_data
        def gds_validate_double(self, input_data, node, input_name=''):
            return input_data
        def gds_format_double_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_double_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of doubles')
            return input_data
        def gds_format_boolean(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean(self, input_data, node, input_name=''):
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                if value not in ('true', '1', 'false', '0', ):
                    raise_parse_error(node, 'Requires sequence of booleans ("true", "1", "false", "0")')
            return input_data
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = 'ascii'
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')

#
# Support/utility functions.
#

def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')

def quote_xml(inStr):
    if not inStr:
        return ''
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1

def quote_attrib(inStr):
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1

def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1

def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text

def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


class GDSParseError(Exception):
    pass

def raise_parse_error(node, msg):
    if XMLParser_import_library == XMLParser_import_lxml:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    else:
        msg = '%s (element %s)' % (msg, node.tag, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace, pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip(): 
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, namespace, name, pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (self.name, self.value, self.name))
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s",\n' % \
                (self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0):
        self.name = name
        self.data_type = data_type
        self.container = container
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container

def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#

class MemoryObjectType(cybox_common_types_1_0.DefinedObjectType):
    """The MemoryObjectType type is intended to characterize generic memory
    objects.The isinjected attribute specifies whether or not the
    particular memory object has had data/code injected into it by
    another process.The ismapped attribute specified whether or not
    the particular memory object has been assigned a byte-for-byte
    correlation with some portion of a file or file-like
    resource.The isprotected attribute specifies whether or not the
    particular memory object is protected (read/write only from the
    process that allocated it)."""
    subclass = None
    superclass = cybox_common_types_1_0.DefinedObjectType
    def __init__(self, object_reference=None, is_protected=None, is_injected=None, is_mapped=None, Hashes=None, Name=None, Region_Size=None, Region_Start_Address=None):
        super(MemoryObjectType, self).__init__(object_reference, )
        self.is_protected = _cast(bool, is_protected)
        self.is_injected = _cast(bool, is_injected)
        self.is_mapped = _cast(bool, is_mapped)
        self.Hashes = Hashes
        self.Name = Name
        self.Region_Size = Region_Size
        self.Region_Start_Address = Region_Start_Address
    def factory(*args_, **kwargs_):
        if MemoryObjectType.subclass:
            return MemoryObjectType.subclass(*args_, **kwargs_)
        else:
            return MemoryObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Hashes(self): return self.Hashes
    def set_Hashes(self, Hashes): self.Hashes = Hashes
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def validate_StringObjectAttributeType(self, value):
        # Validate type cybox_common_types_1_0.StringObjectAttributeType, a restriction on None.
        pass
    def get_Region_Size(self): return self.Region_Size
    def set_Region_Size(self, Region_Size): self.Region_Size = Region_Size
    def validate_UnsignedLongObjectAttributeType(self, value):
        # Validate type cybox_common_types_1_0.UnsignedLongObjectAttributeType, a restriction on None.
        pass
    def get_Region_Start_Address(self): return self.Region_Start_Address
    def set_Region_Start_Address(self, Region_Start_Address): self.Region_Start_Address = Region_Start_Address
    def validate_HexBinaryObjectAttributeType(self, value):
        # Validate type cybox_common_types_1_0.HexBinaryObjectAttributeType, a restriction on None.
        pass
    def get_is_protected(self): return self.is_protected
    def set_is_protected(self, is_protected): self.is_protected = is_protected
    def get_is_injected(self): return self.is_injected
    def set_is_injected(self, is_injected): self.is_injected = is_injected
    def get_is_mapped(self): return self.is_mapped
    def set_is_mapped(self, is_mapped): self.is_mapped = is_mapped
    def export(self, outfile, level, namespace_='MemoryObj:', name_='MemoryObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MemoryObjectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='MemoryObj:', name_='MemoryObjectType'):
        super(MemoryObjectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='MemoryObjectType')
        if self.is_protected is not None and 'is_protected' not in already_processed:
            already_processed.append('is_protected')
            outfile.write(' is_protected="%s"' % self.gds_format_boolean(self.gds_str_lower(str(self.is_protected)), input_name='is_protected'))
        if self.is_injected is not None and 'is_injected' not in already_processed:
            already_processed.append('is_injected')
            outfile.write(' is_injected="%s"' % self.gds_format_boolean(self.gds_str_lower(str(self.is_injected)), input_name='is_injected'))
        if self.is_mapped is not None and 'is_mapped' not in already_processed:
            already_processed.append('is_mapped')
            outfile.write(' is_mapped="%s"' % self.gds_format_boolean(self.gds_str_lower(str(self.is_mapped)), input_name='is_mapped'))
    def exportChildren(self, outfile, level, namespace_='MemoryObj:', name_='MemoryObjectType', fromsubclass_=False, pretty_print=True):
        super(MemoryObjectType, self).exportChildren(outfile, level, 'MemoryObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Hashes is not None:
            self.Hashes.export(outfile, level, 'MemoryObj:', name_='Hashes', pretty_print=pretty_print)
        if self.Name is not None:
            self.Name.export(outfile, level, 'MemoryObj:', name_='Name', pretty_print=pretty_print)
        if self.Region_Size is not None:
            self.Region_Size.export(outfile, level, 'MemoryObj:', name_='Region_Size', pretty_print=pretty_print)
        if self.Region_Start_Address is not None:
            self.Region_Start_Address.export(outfile, level, 'MemoryObj:', name_='Region_Start_Address', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Hashes is not None or
            self.Name is not None or
            self.Region_Size is not None or
            self.Region_Start_Address is not None or
            super(MemoryObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='MemoryObjectType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.is_protected is not None and 'is_protected' not in already_processed:
            already_processed.append('is_protected')
            showIndent(outfile, level)
            outfile.write('is_protected = %s,\n' % (self.is_protected,))
        if self.is_injected is not None and 'is_injected' not in already_processed:
            already_processed.append('is_injected')
            showIndent(outfile, level)
            outfile.write('is_injected = %s,\n' % (self.is_injected,))
        if self.is_mapped is not None and 'is_mapped' not in already_processed:
            already_processed.append('is_mapped')
            showIndent(outfile, level)
            outfile.write('is_mapped = %s,\n' % (self.is_mapped,))
        super(MemoryObjectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(MemoryObjectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Hashes is not None:
            showIndent(outfile, level)
            outfile.write('Hashes=model_.cybox_common_types_1_0.HashListType(\n')
            self.Hashes.exportLiteral(outfile, level, name_='Hashes')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Name is not None:
            showIndent(outfile, level)
            outfile.write('Name=model_.cybox_common_types_1_0.StringObjectAttributeType(\n')
            self.Name.exportLiteral(outfile, level, name_='Name')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Region_Size is not None:
            showIndent(outfile, level)
            outfile.write('Region_Size=model_.cybox_common_types_1_0.UnsignedLongObjectAttributeType(\n')
            self.Region_Size.exportLiteral(outfile, level, name_='Region_Size')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Region_Start_Address is not None:
            showIndent(outfile, level)
            outfile.write('Region_Start_Address=model_.cybox_common_types_1_0.HexBinaryObjectAttributeType(\n')
            self.Region_Start_Address.exportLiteral(outfile, level, name_='Region_Start_Address')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('is_protected', node)
        if value is not None and 'is_protected' not in already_processed:
            already_processed.append('is_protected')
            if value in ('true', '1'):
                self.is_protected = True
            elif value in ('false', '0'):
                self.is_protected = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('is_injected', node)
        if value is not None and 'is_injected' not in already_processed:
            already_processed.append('is_injected')
            if value in ('true', '1'):
                self.is_injected = True
            elif value in ('false', '0'):
                self.is_injected = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('is_mapped', node)
        if value is not None and 'is_mapped' not in already_processed:
            already_processed.append('is_mapped')
            if value in ('true', '1'):
                self.is_mapped = True
            elif value in ('false', '0'):
                self.is_mapped = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(MemoryObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Hashes':
            obj_ = cybox_common_types_1_0.HashListType.factory()
            obj_.build(child_)
            self.set_Hashes(obj_)
        elif nodeName_ == 'Name':
            obj_ = cybox_common_types_1_0.StringObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Name(obj_)
        elif nodeName_ == 'Region_Size':
            obj_ = cybox_common_types_1_0.UnsignedLongObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Region_Size(obj_)
        elif nodeName_ == 'Region_Start_Address':
            obj_ = cybox_common_types_1_0.HexBinaryObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Region_Start_Address(obj_)
        super(MemoryObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class MemoryObjectType

USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)

def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = globals().get(tag)
    return tag, rootClass

def parse(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Memory_Region'
        rootClass = MemoryObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='',
        pretty_print=True)
    return rootObj

def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Memory_Region'
        rootClass = MemoryObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="Memory_Region",
        namespacedef_='')
    return rootObj

def parseLiteral(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Memory_Region'
        rootClass = MemoryObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('#from temp import *\n\n')
    sys.stdout.write('import temp as model_\n\n')
    sys.stdout.write('rootObj = model_.rootTag(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
    sys.stdout.write(')\n')
    return rootObj

def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()

if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

__all__ = [
    "MemoryObjectType"
    ]