#!/bin/sh
curl https://github.com/FreeRDP/FreeRDP  2>/dev/null | grep 'Release '|sed -e 's,.*<span.*Release ,,;s,</span>.*,,'

