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


import argparse
import types

from tfs.common.TFBaseSettings import TFBaseSettings
#import tfs.common.UnicodeCharacterNames as UnicodeCharacterNames


class AutokernSettings(TFBaseSettings):

    def glyphCategoriesType(self, value):
        if type(value) not in ( types.StringType,
                                types.UnicodeType, ):
            raise argparse.ArgumentTypeError('Invalid value: ' + value)
        import AutokernGlyphClasses
        categories = AutokernGlyphClasses.unicodedataCategoryMap.keys()
        if value in categories:
            return value
        if value[-1] == '*':
            valueMajor = value[:-1]
            categoriesMajor = set([category[0] for category in categories])
            if valueMajor in categoriesMajor:
                return value
        raise argparse.ArgumentTypeError('Invalid unicodedata category value: ' + value)


    def boundedFloat(self, minValue, maxValue):
        def typeFunction(value):
            try:
                floatValue = float(value)
            except ValueError, e:
                raise argparse.ArgumentTypeError('Invalid value: ' + value)
            if not (minValue <= floatValue <= maxValue):
                raise argparse.ArgumentTypeError('%0.3f not between %0.3f and %0.3f' % ( floatValue, minValue, maxValue) )
            return floatValue
        return typeFunction

    def boundedInt(self, minValue=None, maxValue=None):
        def typeFunction(value):
            try:
                intValue = int(value)
            except ValueError, e:
                raise argparse.ArgumentTypeError('Invalid value: ' + value)
            if minValue is not None and maxValue is not None:
                if not (minValue <= intValue <= maxValue):
                    raise argparse.ArgumentTypeError('%d not between %d and %d' % ( intValue, minValue, maxValue) )
            elif minValue is not None:
                if not (minValue <= intValue):
                    raise argparse.ArgumentTypeError('%d not greater than %d' % ( intValue, minValue) )
            elif maxValue is not None:
                if not (intValue <= maxValue):
                    raise argparse.ArgumentTypeError('%d not less than %d' % ( intValue, maxValue) )
            return intValue
        return typeFunction

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

    def dumpCommandLineSettings(self):
        return False

    def createParser(self):

        parser = argparse.ArgumentParser(description='...')

        parser.add_argument('--ufo-src-path',
                            type=self.ufoSrcFolderType,
                            help='The UFO source file to kern.',
                            required=True)
        parser.add_argument('--ufo-dst-path',
                            type=self.ufoDstFolderType,
                            help='The UFO destination file.',
                            required=True)
        parser.add_argument('--log-path',
                            type=self.dstFolderType,
                            help='''
                            Optional folder in which to write HTML logs.
                            Note: Some logging configurations dramatically worsen performance.
                            ''')
        parser.add_argument('--write-kerning-pair-logs',
                            action='store_true',
                            help='Write HTML logs for each kerning pair.')
        parser.add_argument('--disparity-log-count',
                            type=self.boundedInt(minValue=0),
                            default=10,
                            help='The number of disparity logs to write. Default: 10')
        parser.add_argument('--log-basic-pairs',
                            action='store_true',
                            help='''
                            If present, Autokern will write the "basic pairs" logs which can be used for proofing.
                            NOTE: these logs are time-consuming to generate.
                            ''')

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
        parser.add_argument('--kern-samples-only',
                            action='store_true',
                            help='''If present, Autokern will only kern the glyph pairs used in the sample text log.
                            Other glyphs will be not kerned.
                            Overridden by the --glyph-pairs-to-kern and --glyphs-to-kern arguments.
                            ''')
        parser.add_argument('--sample-texts',
#                            type=self.codePointType,
                            nargs='+',
                            help='''A list of short texts to render in the "sample text" log.
                            ''')

#        parser.add_argument('--kerning-strength',
#                            type=self.boundedFloat(0.0, +1.0),
#                            default=0.75,
#                            help='''
#                            The lower the value, the less glyphs will "intrude" into the whitespace between them.
#                            0.0 <= x <= 1.0.
#                            Default: 0.75 em
#                            ''')
        parser.add_argument('--tracking-ems',
                            type=self.boundedFloat(-1.0, +1.0),
                            default=0.0,
                            help='''
                            A constant padding value for all kerning pairs in ems.
                            Can be negative.
                            -1.0 <= x <= +1.0.
                            Default: 0.0 em
                            ''')
        parser.add_argument('--min-distance-ems',
                            type=self.boundedFloat(0.0, 1.0),
#                            default=0.025,
                            default=0.0,
                            help='''
                            The absolute minimum distance between glyphs in ems.
                            0.0 <= x <= 1.0.
                            Default: 0.0 em
                            ''')
        parser.add_argument('--max-distance-ems',
                            type=self.boundedFloat(0.0, 1.0),
#                            default=0.08,
                            default=0.0,
                            help='''
                            The absolute maximum distance between glyphs in ems.
                            0.0 <= x <= 1.0.
                            Default: 0.0 em.
                            ''')

        parser.add_argument('--only-modify-side-bearings',
                            action='store_true',
                            help='''
                            If present, Autokern only performs auto-spacing and not auto-kerning.
                            Autokern will update the side bearings and discard the current kerning table.
                            Cannot be used with --do-not-modify-side-bearings.
                            ''')
        parser.add_argument('--do-not-modify-side-bearings',
                            action='store_true',
                            help='''
                            If present, Autokern only performs auto-kerning and not auto-spacing.
                            Autokern will preserve the current side bearings.
                            Cannot be used with --do-not-modify-side-bearings.
                            ''')

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
                            type=self.boundedFloat(0.001, 1.0),
                            default=0.005,
                            help='''
                            Precision of the algorithm.
                            Lower values are more precise but slower.
                            Use a precision of 5 or less for accurate results.
                            0.0 <= x <= 1.0.
                            Default: 0.005.
                            ''')
        parser.add_argument('--intrusion-tolerance-ems',
                            type=self.boundedFloat(0.0, 1.0),
#                            default=0.05,
                            default=0.0,
                            help='''
                            Intrusion tolerance in ems.
                            0.0 <= x <= 1.0.
                            Default: 0.0.
                            ''')
#        parser.add_argument('--intrusion-min-thickness-ems',
#                            type=self.boundedFloat(0.0, 1.0),
#                            default=0.0,
#                            help='''
#                            Minimum effective thickness of intrusion in ems.
#                            0.0 <= x <= 1.0.
#                            Default: 0.0.
#                            ''')
        parser.add_argument('--max-x-extrema-overlap-ems',
                            type=self.boundedFloat(-1.0, 1.0),
#                            default=0.1,
                            default=0.0,
                            help='''
                            The maximum overlap of the x-extrema of the glyphs being kerned in ems.
                            A negative value implies a minimum x-extrema distance.
                            -1.0 <= x <= 1.0.
                            Default: 0.0 em.
                            ''')
#                            Default: 0.1 em.
        parser.add_argument('--x-extrema-overlap-scaling',
                            type=self.boundedFloat(0.0, 1.0),
                            default=1.0,
                            help='''
                            Can be used to scale x-extrema overlap.
                            0.0 <= x <= 1.0.
                            Default: 1.0.
                            ''')
        parser.add_argument('--ignore-x-extrema-overlap-outside-ascender',
                            action='store_true',
                            help='''
                            If present, Autokern ignore x-extrema overlap below the baseline and above the ascender.
                            ''')
        parser.add_argument('--kerning-threshold-ems',
                            type=self.boundedFloat(0.0, 1.0),
                            default=0.01,
                            help='''
                            Kerning values smaller than this threshold will be ignored.
                            0.0 <= x <= 1.0.
                            Default: 0.01 em
                            ''')
        parser.add_argument('--max-kerning-pairs',
                            type=self.boundedInt(minValue=1),
                            help='Limits the number of kerning values.')

#        For example, to use -0.025 em for all punctuation, marks and symbols, use: --max-x-extrema-overlap-ems-per-category P* -0.025 M* -0.025 S* -0.025.
        def addPerCategoryArgument(key, defaultValues=None):
            helpMsg = '''
                        A list of per-category %s values.

                        For example, to use 0.025 em for all punctuation, marks and symbols, use: %s-per-category P* 0.025 M* 0.025 S* 0.025.

                        See %s for more details.
                        See --glyph-categories-to-ignore for an explanation of glyph categories.
                        ''' % (
                               key,
                               key,
                               key,
                               )
            if defaultValues is not None:
                helpMsg += 'Default: %s' % ( ' '.join(defaultValues), )
            argm = {
                    'nargs': '+',
                    'help': helpMsg,
                    }
            if defaultValues is not None:
                argm['default'] = defaultValues
            parser.add_argument('%s-per-category' % key,
                                **argm)

        addPerCategoryArgument('--max-x-extrema-overlap-ems',
                               defaultValues=('P*', '-0.025', 'M*', '-0.025', 'S*', '-0.025', ))
        addPerCategoryArgument('--max-distance-ems')
        addPerCategoryArgument('--min-distance-ems')
        addPerCategoryArgument('--intrusion-tolerance-ems')
        addPerCategoryArgument('--tracking-ems')


        parser.add_argument('--glyph-categories',
                            nargs='*',
                            help='''
                            A list of unicode categories for glyphs.
                            Autokern cannot process a glyph if it can not identify its unicode category.
                            It is only necessary to specify a category with this argument for glyphs
                            whose category can't be identified by normal means.
                            You may use an asterisk as a wildcard.

                            For example, to have cedillacomb treated as a Letter modifier (Lm) and other unknown glyphs to be treated as Other/Unassigned,
                            use: --glyph-categories cedillacomb Lm * Cn

                            See the Unicodedata documentation for a list of glyph categories:
                            http://www.unicode.org/reports/tr44/tr44-4.html#General_Category_Values
                            ''')
#                            Default: Lm Sk C* Z*.
        parser.add_argument('--glyphs-to-ignore',
#                            type=self.codePointType,
                            nargs='+',
                            help='''
                            A list of glyphs to ignore.
                            These glyphs will be not kerned and their side bearings will not be updated.
                            Values may be glyph names (ie. A = A), decimal (ie. 65 = A), or hexidecimal (ie. 0x41 = A).

                            See the Adobe Glyph List for a list of glyph names:
                            partners.adobe.com/public/developer/en/opentype/aglfn13.txt
                            ''')
        parser.add_argument('--glyph-categories-to-ignore',
                            type=self.glyphCategoriesType,
                            nargs='*',
                            default=('Lm', 'Sk', 'C*', 'Z*',),
                            help='''
                            A list of glyph categories to ignore.
                            Glyphs in these categories will be not kerned and their side bearings will not be updated.
                            Categories (ie. Lu = Letter, Uppercase) have a major (ie. Letter) and minor (ie. Uppercase) components.
                            You may use an asterisk in the minor component as a wildcard (ie. L* = all Letters).

                            For example, to ignore Letter modifiers (Lm) and spacing (Zs, Zl, Zp) use: --glyph-categories-to-ignore Lm Z*.

                            See the Unicodedata documentation for a list of glyph categories:
                            http://www.unicode.org/reports/tr44/tr44-4.html#General_Category_Values
                            Default: Lm Sk C* Z*.
                            ''')

        return parser
