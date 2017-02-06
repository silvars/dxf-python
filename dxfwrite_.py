#https://media.readthedocs.org/pdf/dxfwrite/latest/dxfwrite.pdf
from dxfwrite import DXFEngine as dxf


drawing = dxf.drawing('dxfwrite_1.dxf')
style = dxf.style('minha_fonte1', font='MITSUBISHI 2015')
drawing.styles.clear()
drawing.styles.add(style)
drawing.add_style('minha_fonte1')
text = dxf.text('* XX 872349 *', (2.0, 2.0), height=0.7)
drawing.add(text)
drawing.save()

drawing = dxf.drawing('dxfwrite_2.dxf')
style = dxf.style('minha_fonte2', font='KacstOne')
drawing.styles.clear()
drawing.styles.add(style)
drawing.add_style('minha_fonte2')
text = dxf.text('* XX 872349 *', (2.0, 2.0), height=0.7)
drawing.add(text)

drawing.save()

