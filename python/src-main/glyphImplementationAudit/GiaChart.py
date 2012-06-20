'''
robofont-extensions-and-scripts
GiaChart.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com

Apache License

Version 2.0, January 2004

http://www.apache.org/licenses/

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

1. Definitions.

"License" shall mean the terms and conditions for use, reproduction, and distribution as defined by Sections 1 through 9 of this document.

"Licensor" shall mean the copyright owner or entity authorized by the copyright owner that is granting the License.

"Legal Entity" shall mean the union of the acting entity and all other entities that control, are controlled by, or are under common control with that entity. For the purposes of this definition, "control" means (i) the power, direct or indirect, to cause the direction or management of such entity, whether by contract or otherwise, or (ii) ownership of fifty percent (50%) or more of the outstanding shares, or (iii) beneficial ownership of such entity.

"You" (or "Your") shall mean an individual or Legal Entity exercising permissions granted by this License.

"Source" form shall mean the preferred form for making modifications, including but not limited to software source code, documentation source, and configuration files.

"Object" form shall mean any form resulting from mechanical transformation or translation of a Source form, including but not limited to compiled object code, generated documentation, and conversions to other media types.

"Work" shall mean the work of authorship, whether in Source or Object form, made available under the License, as indicated by a copyright notice that is included in or attached to the work (an example is provided in the Appendix below).

"Derivative Works" shall mean any work, whether in Source or Object form, that is based on (or derived from) the Work and for which the editorial revisions, annotations, elaborations, or other modifications represent, as a whole, an original work of authorship. For the purposes of this License, Derivative Works shall not include works that remain separable from, or merely link (or bind by name) to the interfaces of, the Work and Derivative Works thereof.

"Contribution" shall mean any work of authorship, including the original version of the Work and any modifications or additions to that Work or Derivative Works thereof, that is intentionally submitted to Licensor for inclusion in the Work by the copyright owner or by an individual or Legal Entity authorized to submit on behalf of the copyright owner. For the purposes of this definition, "submitted" means any form of electronic, verbal, or written communication sent to the Licensor or its representatives, including but not limited to communication on electronic mailing lists, source code control systems, and issue tracking systems that are managed by, or on behalf of, the Licensor for the purpose of discussing and improving the Work, but excluding communication that is conspicuously marked or otherwise designated in writing by the copyright owner as "Not a Contribution."

"Contributor" shall mean Licensor and any individual or Legal Entity on behalf of whom a Contribution has been received by Licensor and subsequently incorporated within the Work.

2. Grant of Copyright License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works in Source or Object form.

3. Grant of Patent License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as stated in this section) patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Work, where such license applies only to those patent claims licensable by such Contributor that are necessarily infringed by their Contribution(s) alone or by combination of their Contribution(s) with the Work to which such Contribution(s) was submitted. If You institute patent litigation against any entity (including a cross-claim or counterclaim in a lawsuit) alleging that the Work or a Contribution incorporated within the Work constitutes direct or contributory patent infringement, then any patent licenses granted to You under this License for that Work shall terminate as of the date such litigation is filed.

4. Redistribution. You may reproduce and distribute copies of the Work or Derivative Works thereof in any medium, with or without modifications, and in Source or Object form, provided that You meet the following conditions:

You must give any other recipients of the Work or Derivative Works a copy of this License; and

You must cause any modified files to carry prominent notices stating that You changed the files; and

You must retain, in the Source form of any Derivative Works that You distribute, all copyright, patent, trademark, and attribution notices from the Source form of the Work, excluding those notices that do not pertain to any part of the Derivative Works; and

If the Work includes a "NOTICE" text file as part of its distribution, then any Derivative Works that You distribute must include a readable copy of the attribution notices contained within such NOTICE file, excluding those notices that do not pertain to any part of the Derivative Works, in at least one of the following places: within a NOTICE text file distributed as part of the Derivative Works; within the Source form or documentation, if provided along with the Derivative Works; or, within a display generated by the Derivative Works, if and wherever such third-party notices normally appear. The contents of the NOTICE file are for informational purposes only and do not modify the License. You may add Your own attribution notices within Derivative Works that You distribute, alongside or as an addendum to the NOTICE text from the Work, provided that such additional attribution notices cannot be construed as modifying the License. You may add Your own copyright statement to Your modifications and may provide additional or different license terms and conditions for use, reproduction, or distribution of Your modifications, or for any such Derivative Works as a whole, provided Your use, reproduction, and distribution of the Work otherwise complies with the conditions stated in this License.

5. Submission of Contributions. Unless You explicitly state otherwise, any Contribution intentionally submitted for inclusion in the Work by You to the Licensor shall be under the terms and conditions of this License, without any additional terms or conditions. Notwithstanding the above, nothing herein shall supersede or modify the terms of any separate license agreement you may have executed with Licensor regarding such Contributions.

6. Trademarks. This License does not grant permission to use the trade names, trademarks, service marks, or product names of the Licensor, except as required for reasonable and customary use in describing the origin of the Work and reproducing the content of the NOTICE file.

7. Disclaimer of Warranty. Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

8. Limitation of Liability. In no event and under no legal theory, whether in tort (including negligence), contract, or otherwise, unless required by applicable law (such as deliberate and grossly negligent acts) or agreed to in writing, shall any Contributor be liable to You for damages, including any direct, indirect, special, incidental, or consequential damages of any character arising as a result of this License or out of the use or inability to use the Work (including but not limited to damages for loss of goodwill, work stoppage, computer failure or malfunction, or any and all other commercial damages or losses), even if such Contributor has been advised of the possibility of such damages.

9. Accepting Warranty or Additional Liability. While redistributing the Work or Derivative Works thereof, You may choose to offer, and charge a fee for, acceptance of support, warranty, indemnity, or other liability obligations and/or rights consistent with this License. However, in accepting such obligations, You may act only on Your own behalf and on Your sole responsibility, not on behalf of any other Contributor, and only if You agree to indemnify, defend, and hold each Contributor harmless for any liability incurred by, or claims asserted against, such Contributor by reason of your accepting any such warranty or additional liability.

END OF TERMS AND CONDITIONS
'''


import os
import pystache
import unicodedata

from tfs.common.UnicodeCharacterNames import getUnicodeCharacterName, getUnicodeLongName, getUnicodeShortName
import tfs.common.TFSProject as TFSProject
from autokern.AutokernGlyphClasses import unicodedataCategoryMap


values = [0x0020, 0x0061, 0x0065, 0x0042, 0x0041, 0x0069, 0x0043, 0x0045, 0x0062, 0x006F, 0x006C, 0x0046, 0x0074, 0x006D, 0x0073, 0x004E, 0x0072, 0x0044, 0x004C, 0x0047, 0x0049, 0x0064, 0x004B, 0x0066, 0x0079, 0x004D, 0x0063, 0x0067, 0x0068, 0x0076, 0x0077, 0x0048, 0x0078, 0x0059, 0x004F, 0x0057, 0x004A, 0x0056, 0x005A, 0x006A, 0x0058, 0x0053, 0x006E, 0x0055, 0x006B, 0x0052, 0x0070, 0x0071, 0x0050, 0x0054, 0x0075, 0x0051, 0x007A, 0x0032, 0x0033, 0x0031, 0x0034, 0x0036, 0x0035, 0x0037, 0x0038, 0x0039, 0x0030, 0x002E, 0x002C, 0x0021, 0x003A, 0x003F, 0x003B, 0x002D, 0x0028, 0x0027, 0x0029, 0x0022, 0x0026, 0x002F, 0x0024, 0x002A, 0x003D, 0x002B, 0x0025, 0x005C, 0x005F, 0x005B, 0x005D, 0x003C, 0x003E, 0x0060, 0x0023, 0x0040, 0x2019, 0x2018, 0x201D, 0x201C, 0x007C, 0x005E, 0x007B, 0x007D, 0x007E, 0x00C6, 0x00E6, 0x00A1, 0x00C4, 0x00BF, 0x00C5, 0x00E4, 0x00D6, 0x00F6, 0x00FC, 0x00E5, 0x00DC, 0x00F8, 0x00CB, 0x00EB, 0x00CA, 0x00E9, 0x00B4, 0x00CF, 0x00A8, 0x00A2, 0x00E1, 0x00D8, 0x00C9, 0x00CD, 0x00E8, 0x00EA, 0x00D3, 0x00C8, 0x00CE, 0x00F1, 0x00D4, 0x00D2, 0x00E3, 0x00F9, 0x00D5, 0x00D1, 0x00C1, 0x00FA, 0x00E0, 0x00EF, 0x00C2, 0x00CC, 0x00FB, 0x00F5, 0x00E2, 0x00F3, 0x00ED, 0x00C3, 0x00EC, 0x00F2, 0x00EE, 0x00F4, 0x00C0, 0x00DB, 0x2026, 0x00D9, 0x00DA, 0x00FF, 0x2014, 0x0153, 0x2013, 0x0152, 0x2022, 0x0178, 0x02C6, 0x00DF, 0x00AB, 0x00BB, 0x02DC, 0x00A9, 0x00C7, 0x00A3, 0x00E7, 0x201E, 0x00A0, 0x00AE, 0x201A, 0x00A5, 0x2039, 0x203A, 0x2122, 0x00B8, 0x00B7, 0x0160, 0x00F7, 0x00B6, 0x00B1, 0x2030, 0x0161, 0x2020, 0x00A7, 0x2021, 0x00D7, 0x00B0, 0x00A4, 0x00BA, 0x00FD, 0x00AA, 0x0192, 0x00DD, 0x00AF, 0x00B5, 0x00AC, 0x00DE, 0x00D0, 0x00FE, 0x00F0, 0x02C7, 0x0131, 0x02DA, 0x00A6, 0x017D, 0x017E, 0x00BD, 0x00BC, 0x00B2, 0x00B3, 0x00B9, 0x00BE, 0x20AC, 0x00AD, 0x2219, 0x02D8, 0x02D9, 0x02DB, 0x2212, 0x0141, 0x0142, 0x02C9, 0x2215, 0x2044, 0x02DD, 0x221A, 0x2264, 0x2265, 0x2260, 0x2202, 0x03BC, 0x221E, 0x2248, 0x222B, 0x220F, 0x25CA, 0x2010, 0x2206, 0x03C0, 0x03A9, 0x2211, 0xFB01, 0xFB02, 0x2126, 0x0119, 0x0117, 0x011A, 0x2113, 0x0113, 0x0112, 0x0116, 0x011E, 0x011F, 0x011B, 0x0130, 0x0139, 0x212E, 0x013A, 0x0114, 0x0122, 0x012E, 0x012A, 0x012B, 0x0115, 0x0118, 0xF001, 0x012F, 0x0123, 0x0136, 0x013B, 0x0137, 0xF002, 0x0106, 0x0107, 0x010C, 0x010D, 0x0111, 0x0120, 0x0121, 0x011C, 0x015E, 0x0105, 0x0179, 0x0104, 0x015F, 0x011D, 0x017A, 0x0110, 0x0162, 0x0126, 0x015A, 0x0127, 0x0124, 0x0163, 0x017B, 0x0102, 0x0158, 0x015B, 0x010E, 0x012D, 0x016E, 0x013D, 0x0147, 0x017C, 0x0103, 0x0164, 0x0150, 0x0159, 0x0148, 0x016F, 0x0170, 0x013E, 0x0151, 0x010F, 0x0171, 0x0165, 0x0394, 0x0133, 0x0132, 0x0173, 0x0145, 0x0125, 0x0100, 0x012C, 0x0172, 0x0101, 0x013C, 0x0146, 0x0156, 0x0144, 0x0143, 0x0129, 0x0128, 0x0157, 0x014D, 0x016A, 0x016B, 0xE001, 0x0154, 0x0155, 0x014C, 0x0138, 0x0134, 0x0135, 0x013F, 0x0140, 0xE000, 0xF000, 0xFB00, 0x207F, 0xFB03, 0xFB04, 0x0218, 0x0219, 0x215C, 0x215D, 0x215B, 0x215E, 0x010B, 0x0176, 0x2074, 0x0174, 0x010A, 0x016D, 0x2192, 0x2190, 0x0177, 0x20A3, 0xE002, 0x015D, 0x0108, 0x015C, 0x1E84,]

def writeMustacheLog(mustacheFilename, dstFile, mustacheVars, replaceMap=None):
    mustacheFile = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'data', mustacheFilename))
    if not (os.path.exists(mustacheFile) and os.path.isfile(mustacheFile)):
        raise Exception('Invalid mustacheFile: ' + mustacheFile)
    with open(mustacheFile, 'rt') as f:
        mustache_template = f.read()

    mustacheMap = {
                   }
    mustacheMap.update(mustacheVars)

    logHtml = pystache.render(mustache_template, mustacheMap)

    if replaceMap:
        for key, value in replaceMap.items():
            logHtml = logHtml.replace(key, value)

#    dstFile = os.path.abspath(os.path.join(self.html_folder, dstFilename))
    with open(dstFile, 'wt') as f:
        # TODO: explicitly encode unicode
        f.write(logHtml)


values.sort()
glyphsMaps = []
for value in values:
#    print 'value', value, type(value)

    unicode_category = '?'
    try:
        uc = unichr(value)
        if uc is not None:
            unicode_category = unicodedata.category(uc)
    except UnicodeEncodeError:
        pass

    category_color = '3f3faf'
    category_prefix = unicode_category[0]
    category_colorMap = {
        'L': '3f3f3f',
        'M': 'ef3f3f',
        'N': '3fef3f',
        'P': '3f3fef',
        'Z': '3fefef',
        'S': 'ef3fef',
        'C': 'efef3f',
        }
    if category_prefix in category_colorMap:
        category_color = category_colorMap[category_prefix]
#        L Letter
#        M Mark
#        N Number
#        P Punctuation
#        Z Separator
#        S Symbol
#        C Other
#        '''

    categoryName = 'Unknown'
    categoryMap = unicodedataCategoryMap.get(unicode_category, None)
    if categoryMap is not None:
        categoryName = categoryMap.major + ' ' + categoryMap.minor


    glyphsMaps.append({
                       'glyphHex': '%X' % value,
                       'shortName': getUnicodeShortName(value, ignoreUnknown=True),
                       'longName': getUnicodeLongName(value, ignoreUnknown=True),
                       'glyphName': getUnicodeCharacterName(value, ignoreUnknown=True),
                       'unicode_category': unicode_category,
                       'category_color': category_color,
                       'categoryName': categoryName,
                       })

mustacheMap = {
               'glyphsMaps': glyphsMaps,
               'pageTitle': 'Unicode Categories Chart',
               }
mustacheFilename = 'gia_chart_template.txt'
dstFilename = 'glyph_categories.html'
dstFile = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'out', dstFilename))
print 'dstFile', dstFile
writeMustacheLog(mustacheFilename, dstFile, mustacheMap)


print
print 'complete.'
