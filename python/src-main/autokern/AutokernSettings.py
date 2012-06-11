'''
robofont-extensions-and-scripts
AutokernSettings.py

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


from tfs.common.TFBaseSettings import TFBaseSettings
#import tfs.common.UnicodeCharacterNames as UnicodeCharacterNames
import argparse


class AutokernSettings(TFBaseSettings):

#    def codePointType(self, value):
#        if value.startswith('0x'):
#            try:
#                codePoint = int(value, 16)
#            except ValueError, e:
#                raise argparse.ArgumentTypeError('Invalid hexidecimal code point: ' + value)
#            try:
#                name = UnicodeCharacterNames.getUnicodeCharacterName(codePoint)
#                return name
#            except ValueError, e:
#                raise argparse.ArgumentTypeError('Unknown hexidecimal code point: ' + value)
#        else:
#            try:
#                codePoint = int(value)
#            except ValueError, e:
#                '''
#                ignore
#                '''
#                pass
#
#                raise argparse.ArgumentTypeError('Not a valid hexidecimal code point: ' + value)
#        el
#        value = self.cleanupPath(value)
#        self.assertExists(value)
#        if os.path.isfile(value):
#            msg = "%s is not a file" % value
#            raise argparse.ArgumentTypeError(msg)
#        return value


    def em01Type(self, value):
        try:
            value = float(value)
        except ValueError, e:
            raise argparse.ArgumentTypeError('Invalid em value: ' + value)

        if value < 0.0 or value > 1.0:
            raise argparse.ArgumentTypeError('Invalid em value: ' + value)
        return value


    def createParser(self):

        parser = argparse.ArgumentParser(description='...')

        parser.add_argument('--ufo-src',
                            type=self.ufoSrcFolderType,
                            help='The UFO source file to kern.',
                            required=True)
        parser.add_argument('--ufo-dst',
                            type=self.ufoDstFolderType,
                            help='The UFO destination file.',
                            required=True)
        parser.add_argument('--log-dst',
                            type=self.dstFolderType,
                            help='''
                            Optional folder in which to write HTML logs.
                            Note: Writing the HTML logs dramatically worsens performance.
                            CAUTION: This folder will be completely overwritten.
                            ''')
        parser.add_argument('--skip-kerning-pair-logs',
                            action='store_true',
                            help='Do not write HTML logs for each kerning pair.')
        parser.add_argument('--disparity-log-count',
                            type=int,
                            default=10,
                            help='The number of disparity logs to write. Default: 10')

        parser.add_argument('--glyph-pairs-to-kern',
#                            type=self.codePointType,
                            nargs='+',
                            help='''A list of glyph pairs to kern.
                            Other glyphs pairs will be not kerned.
                            Values may be glyph names (ie. A = A), decimal (ie. 65 = A), or hexidecimal (ie. 0x41 = A).
                            To kern uppercase T against numeral 4 and lowercase e: "--glyph-pairs-to-kern T four T e".
                            Overrides the --glyphs-to-kern argument.
                            If used, no side bearings are adjusted.

                            See the Adobe Glyph List for a list of glyph names:
                            partners.adobe.com/public/developer/en/opentype/aglfn13.txt
                            ''')
        parser.add_argument('--glyphs-to-kern',
#                            type=self.codePointType,
                            nargs='+',
                            help='''A list of glyphs to kern.
                            Other glyphs will be not kerned.
                            Values may be glyph names (ie. A = A), decimal (ie. 65 = A), or hexidecimal (ie. 0x41 = A).
                            To kern uppercase T, numeral 4 and lowercase e against each other: "--glyphs-to-kern T four e".
                            Overridden by the --glyph-pairs-to-kern argument.
                            If used, only side bearings of these glyphs are adjusted.

                            See the Adobe Glyph List for a list of glyph names:
                            partners.adobe.com/public/developer/en/opentype/aglfn13.txt
                            ''')
        parser.add_argument('--min-distance-ems',
                            type=self.em01Type,
                            default=0.025,
                            help='The absolute minimum distance between glyphs in ems. 0.0 <= x <= 1.0. Default: 0.025 em')
        parser.add_argument('--max-distance-ems',
                            type=self.em01Type,
                            default=0.08,
                            help='''
                            The absolute maximum distance between glyphs in ems.
                            0.0 <= x <= 1.0.
                            Default: 0.08 em.
                            ''')

        parser.add_argument('--assess-only',
                            action='store_true',
                            help='''
                            Activates assessment mode which analyzes the input font and suggests --min-distance-ems and --max-distance-ems values.
                            In assessment mode, no kerning is performed and no output is written.
                            ''')

        parser.add_argument('--do-not-modify-side-bearings',
                            action='store_true',
                            help='Preserves the current side bearings.')
        parser.add_argument('--allow-negative-side-bearings',
                            action='store_true',
                            help='Allows side bearings that intrude within the x-extrema of the glyph.')

        # TODO: not yet supported.
#        parser.add_argument('--slope-rise',
#                            type=float,
#                            default=1,
#                            help='The slope of oblique fonts is defined as rise/run (1.0/0.0 for non-oblique fonts).')
#        parser.add_argument('--slope-run',
#                            type=float,
#                            default=0,
#                            help='The slope of oblique fonts is defined as rise/run (1.0/0.0 for non-oblique fonts).')

        parser.add_argument('--precision-ems',
                            type=self.em01Type,
                            default=0.005,
                            help='''
                            Precision of the algorithm.
                            Lower values are more precise but slower.
                            Use a precision of 5 or less for accurate results.
                            0.0 <= x <= 1.0.
                            Default: 0.005.
                            ''')
        parser.add_argument('--intrusion-tolerance-ems',
                            type=self.em01Type,
                            default=0.05,
                            help='''
                            Intrusion tolerance in ems.
                            0.0 <= x <= 1.0.
                            Default: 0.1.
                            ''')
        parser.add_argument('--max-x-extrema-overlap-ems',
                            type=self.em01Type,
                            default=0.1,
                            help='''
                            The maximum overlap of the x-extrema of the glyphs being kerned in ems.
                            0.0 <= x <= 1.0.
                            Default: 0.1 em.
                            ''')
#        parser.add_argument('--min-non-intrusion-ems',
#                            type=self.em01Type,
#                            default=0.2,
#                            help='The minimum non-intruding height in ems.  0.0 <= x <= 1.0. Default: 0.2 em')
        parser.add_argument('--kerning-threshold-ems',
                            type=self.em01Type,
                            default=0.01,
                            help='Kerning values smaller than this threshold will be ignored.  0.0 <= x <= 1.0. Default: 0.01 em')

        return parser
