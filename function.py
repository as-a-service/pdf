import os

from flask import send_file
from subprocess import call

def trace(request):
    bmp_location = '/tmp/bmp/'
    traces_location = '/tmp/traces/'
    svg_name = 'traced'
    svg_filename = traces_location + svg_name + '.svg'

    input_image_file = 'head-orig3.png'
    bmp_image_file = bmp_location + 'temp.bmp'

    if not os.path.exists(bmp_location):
        os.makedirs(bmp_location)
    if not os.path.exists(traces_location):
        os.makedirs(traces_location)

    # Convert image to .bmp
    call('convert %s %s' % (input_image_file, bmp_image_file), shell=True)
    
    # Trace .bmp to .svg
    call('potrace %s -o %s --svg' % (bmp_image_file, svg_filename), shell=True)
    
    return send_file(svg_filename, mimetype='image/svg+xml')