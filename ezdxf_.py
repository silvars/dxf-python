#https://media.readthedocs.org/pdf/ezdxf/latest/ezdxf.pdf
import ezdxf

dwg = ezdxf.new('AC1009') # TEXT is a basic entity and exists in every DXF standard
msp = dwg.modelspace()
# use set_pos() for proper TEXT alignment - the relations between halign, valign, insert and align_point are tricky.
msp.add_text("* YU 908643 *").set_pos((2, 3), align='MIDDLE_RIGHT')

dwg.saveas("ezdxf_.dxf")
