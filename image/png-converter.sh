#!/bin/bash
#convert
for image in *.jpg; do
        convert  "$image"  "${image%.jpg}.png"
        echo “image $image converted to ${image%.jpg}.png ”
done
exit 0 