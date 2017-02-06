import ezdxf

dwg = ezdxf.new('R12')  # R12 for compatibility R2010 for more features

dwg.styles.new('custom_1', dxfattribs={'font': 'MITSUBISHI 2015.ttf'})  # http://ezdxf.readthedocs.io/en/latest/tables.html#style

# the advantage of dxfattribs={} are simple method signatures, and you can reuse property dicts

# adding text:

msp = dwg.modelspace()

msp.add_text('* EU 872349 *', dxfattribs={ 'insert': (2.0, 2.0),  'height': 0.7})  # maybe with typos http://ezdxf.readthedocs.io/en/latest/entities.html#text

# .add_text() factory functions, work the same way in modelspace, layouts and block layouts.


dwg.saveas('filename.dxf')