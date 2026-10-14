# -*- coding: utf-8 -*-
import re
p = 'DarnaDJ_Updated_Package/theme-Place-dj-com.xml'
data = open(p, 'r', encoding='utf-8').read()
lit = re.findall(r'[\u0600-\u06FF]', data)
print('literal arabic chars in file:', len(lit))
print('backslash-u sequences:', data.count('\\u'))
print('literal region present:', ('\u0642\u0644\u0628 \u062c\u064a\u0628\u0648\u062a\u064a \u0627\u0644\u0645\u062f\u064a\u0646\u0629' in data))
print('literal featured present:', ('\u0639\u0642\u0627\u0631\u0627\u062a \u0645\u0645\u064a\u0632\u0629' in data))
print('literal discovery-card present:', ('discovery-card' in data))
print('literal &quot; count:', data.count('&quot;'))
print('file size:', len(data))
