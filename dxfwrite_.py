#https://media.readthedocs.org/pdf/dxfwrite/latest/dxfwrite.pdf
from dxfwrite import DXFEngine as dxf


drawing = dxf.drawing('dxfwrite_.dxf')
style = dxf.style('custom', font='MITSUBISHI 2015.ttf')
drawing.styles.clear()
drawing.styles.add(style)
drawing.add_style('custom')
text = dxf.text('* EU 872349 *', (2.0, 2.0), height=0.7)
drawing.add(text)

drawing.save()

