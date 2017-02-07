import ezdxf
dwg = ezdxf.new('R12')  
dwg.styles.new('xxxx', dxfattribs={'font': 'MITSUBISHI 2015.ttf'}) 
x = dwg.styles
msp = dwg.modelspace()
msp.add_text('* EU 872349 *', dxfattribs={ 'style': 'xxxx', 'height': 0.7}).set_pos((2, 2), align='LEFT')
dwg.saveas('customFile.dxf')