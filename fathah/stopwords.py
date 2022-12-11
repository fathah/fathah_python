
stop_words_ar=['', 'وأنه', 'وأني', 'الله', 'عددا', 'ولا', 'بها', 'ولكن', 'أنه', 'فهذا', 'ولا', 'بأن', 'فهذا', 'لو', 'فيه', 'يا', 'إذا', 'و', 'منها', 'فيه', 'ذو', 'مما', 'مع', 'وحين', 'ونحو', 'بما', 'ومع', 'وبهم', 'بنا', 'فأي', 'أو', 'به', 'بها', 'ولا', 'ان', 'ولكن', 'ليس', 'بأن', 'عليك', 'ولا', 'إذا', 'فإنه', 'يا', 'بعض', 'ذلك', 'لأن', 'وإن', 'فيه', 'ان', 'أما', 'وأما', 'كما', 'إلا', 'بما', 'عليها', 'وليس', 'له', 'لمن', 'فليس', 'وقد', 'وهو', 'فهنا', 'وكذلك', 'وإذا', 'أيضاً', 'عليك', 'وأنه', 'أيضاً', 'ومن', 'لأنها', 'إليه', 'بن', 'أي', 'بعض', 'عند', 'عليه', 'بل', 'أبو', 'لهم', 'هذا', 'فهذا', 'بها', 'فإنه', 'بذلك', 'وأما', 'وإن', 'وقد', 'وهو', 'هذا', 'بأن', 'وإن', 'إلا', 'بعضكم', 'وكذلك', 'فقد', 'لأنها', 'وحين', 'ولكن', 'إنما', 'عليهم', 'غيرها', 'فيما', 'قال', 'يقول', 'قلت', 'بقوله', 'يقال', 'فقال', 'يقال', 'فقالت', 'كونه', 'بعضها', 'بهذه', 'فلما', 'قيل', 'وعند', 'بهما', 'حينئذ', 'ذوو', 'فقيل', 'وبه', 'وكذا', 'ولهذا', 'الكل', 'ألاَّ', 'بعضه', 'بعضها', 'بعضهم', 'بك', 'كون', 'كوننا', 'كونه', 'بكونها', 'ببعضه', 'بحيث', 'بي', 'ففي', 'ففيه', 'فلم', 'فلما', 'فلو', 'لئلا', 'إِلا', 'إِلاَّ', 'إِلخ', 'اّ', 'اَّ', 'ببعض', 'ببعضها', 'لانه', 'لانها', 'لأنهم', 'لأني', 'لأن', 'لأنه', 'لأنه', 'لذا', 'لذو', 'لذوى', 'لعلهم', 'لك', 'لكل', 'لكلا', 'لكننا', 'لكنني', 'لكنها', 'لكنه', 'لكن', 'لكن', 'لكي', 'لك', 'أما', 'أما', 'وآن', 'وأنا', 'وأنت', 'وإنما', 'انما', 'وانه', 'وأنها', 'وانها', 'وإني', 'وأنه', 'وإلا', 'بعد', 'وبعدها', 'وبعض', 'وبعض', 'وبعضا', 'وذو', 'وذوو', 'وذي', 'وذين', 'ونحن', 'ونحوه', 'ونحوها', 'ونحوهما', 'وهاهو', 'بينك', 'بينها', 'بينهم', 'بينهما', 'كل', 'كلاهما', 'كلهم', 'كونك', 'لعل', 'لعله', 'ولكننا', 'ولكنه', 'ولكني', 'له', 'لها', 'لولا', 'سوف', 'الم', 'وهم', 'ألى', 'ب\u200d', 'بأ', 'فأما', 'فأنت', 'فإنك', 'فإننا', 'فإنها', 'فإنهم', 'فعن', 'فعند', 'فعنه', 'فكانت', 'فكأنه', 'فكأنها', 'فكذلك', 'كن', 'فكيف', 'فلابد', 'فلأننا', 'ما', 'فماذا', 'فمن', 'فمنذ', 'فمنها', 'فهذه', 'فهل', 'فهنالك', 'فهي', 'فيكون', 'فيمكن', 'فيهم', 'فيهما', 'كل', 'كلا', 'كلها', 'كل', 'لان', 'لأن', 'لأنك', 'لأننا', 'لأنهما', 'لهذه', 'لهما', 'ليست', 'ليس', 'لنا', 'هى', 'وإليك', 'أم', 'وإما', 'وبعد', 'وبلا', 'وبينما', 'وتكون', 'وتلك', 'وعليك', 'وعليكم', 'وعليه', 'وعليها', 'وعن', 'وعندما', 'وعندنا', 'وعندي', 'وغير', 'وغيرها', 'وغيرهما', 'وكانا', 'وكأنها', 'وكل', 'وكلا', 'وكنت', 'وكونه', 'وكيف', 'ولأن', 'ولعل', 'وليست', 'وليكون', 'ومما', 'ومنه', 'ومنها', 'وهذه', 'وهكذا', 'وهل', 'وهم', 'وهم', 'وهنا', 'وهناك', 'بنحو', 'فإذا', 'فإذن', 'فأنت', 'فإنه', 'فإنها', 'فبأنه', 'فبماذا', 'فعلى', 'فعندما', 'فكانت', 'فكذلك', 'فكما', 'فلابد', 'فله', 'فما', 'فمادام', 'فماذا', 'فمع', 'فمن', 'فهذه', 'فهل', 'فهم', 'فيهما', 'فيهن', 'كل', 'كلا', 'كلها', 'لاغير', 'لان', 'لأن', 'لأنك', 'لأنه', 'لأنهما', 'لبعض', 'لذي', 'لهذه', 'لهما', 'لهن', 'ه\u200d', 'وألا', 'والا', 'وإلى', 'وإن', 'وإنه', 'فهي', 'فمع', 'فمن', 'وحتى', 'وحينئذ', 'وذاك', 'وذلك', 'وشئ', 'وعن', 'وغير', 'وغيرها', 'وغيرهما', 'وفيما', 'ولابد', 'ولأن', 'ولأن', 'ولأنني', 'ولأنها', 'ولذا', 'ولذي', 'ولغير', 'ولم', 'ومنه', 'ومنها', 'ومنهم', 'وهذان', 'وهذه', 'وهم', 'وهنا', 'وهناك', 'البعض', 'إلخ', 'فكانت', 'فكذلك', 'فكلاهما', 'فكما', 'فله', 'فما', 'فهل', 'فهي', 'ومابعدها', 'ومنه', 'ومنها', 'وهذه', 'وهكذا', 'وهم', 'وهما', 'إلا', 'إليه', 'إليها', 'إما', 'فما', 'فمتى', 'فهؤلاء', 'فهل', 'فهي', 'لتلك', 'لكانت', 'لكون', 'لكونه', 'لكونها', 'ليسا', 'ليست', 'هى', 'وإما', 'وها', 'وهذه', 'وهكذا', 'وهل', 'وهم', 'بعدما', 'بعدمها', 'بعده', 'بعدها', 'فأما', 'فإنا', 'لان', 'لانهما', 'لأنهما', 'لبعض', 'لي', 'ليست', 'ما', 'وثم', 'ولئلا', 'ولذا', 'ولعدم', 'ولعل', 'وليست', 'ومنها', 'وهكذا', 'وهل', 'وهما', 'وهناك', 'أنها', 'إنها', 'أنها', 'أنهما', 'وربما', 'بأنه', 'إلاَ', 'أوَ', 'فلن', 'كمن', 'فمنه', 'وانما', 'إلاّ', 'انذاك', 'أيها', 'في\u200f', 'كأنها', 'لكم', 'وسيتم', 'وعلينا', 'ولن', 'وهنالك', 'أن', 'بشأن', 'بشان', 'بشأنه', 'بشأنها', 'بشأنهمما', 'بينكم', 'بينما', 'بيننا', 'بينه', 'فإلى', 'كأنها', ' كونها', 'لكما', 'وفى', 'وفينا', 'ولدينا', 'ولن', 'ولها', 'ولا', 'أنا', 'فإني', 'فكأنما', 'فكأنما', 'كأنما', 'كأنها', 'وبها', 'إنها', 'فبينما', 'فيمن', 'ألا', 'انك', 'فإني', 'وبذلك', 'وبعضهم', 'وبغير', 'فنقول', 'فهذه', 'فهل', 'فهم', 'فهي', 'بكل', 'ويكون', 'بعدم', 'بعده', 'وما', 'الخ', 'بأي', 'فكم', 'فكل', 'ولذلك', 'إنه', 'بذلك', 'ولو', 'عليها', 'مما', 'لهم', 'افلا', 'اه', 'وإلا', 'وفي', 'وقد', 'مع', 'عليه', 'بل', 'أو', 'إذ', 'إلى', 'عن', 'ذلك', 'وفيه', 'بلا', 'فلا', 'كله', 'وهي', '–', 'عليك', 'ذو', 'بهم', 'وفيها', 'آب', 'آذار', 'وكان', 'لهم', 'ولما', 'آض', 'آل', 'آمينَ', 'آناء', 'آنفا', 'آه', 'آهاً', 'آهٍ', 'آهِ', 'أ', 'أبدا', 'أبريل', 'أبو', 'أبٌ', 'أجل', 'أجمع', 'أحد', 'أخبر', 'أخذ', 'أخو', 'أخٌ', 'أربع', 'أربعاء', 'أربعة', 'أربعمئة', 'أربعمائة', 'أرى', 'أسكن', 'أصبح', 'أصلا', 'أضحى', 'أطعم', 'أعطى', 'أعلم', 'أغسطس', 'أفريل', 'أفعل به', 'أفٍّ', 'أقبل', 'أكتوبر', 'أل', 'ألا', 'ألف', 'ألفى', 'أم', 'أما', 'أمام', 'أمامك', 'أمامكَ', 'أمد', 'أمس', 'أمسى', 'أمّا', 'أن', 'أنا', 'أنبأ', 'أنت', 'أنتم', 'أنتما', 'أنتن', 'أنتِ', 'أنشأ', 'أنه', 'أنًّ', 'أنّى', 'أهلا', 'أو', 'أوت', 'أوشك', 'أول', 'أولئك', 'أولاء', 'أولالك', 'أوّهْ', 'أى', 'أي', 'أيا', 'أيار', 'أيضا', 'أيلول', 'أين', 'أيّ', 'أيّان', 'أُفٍّ', 'ؤ', 'إحدى', 'إذ', 'إذا', 'إذاً', 'إذما', 'إذن', 'إزاء', 'إلى', 'إلي', 'إليكم', 'إليكما', 'إليكنّ', 'إليكَ', 'إلَيْكَ', 'إلّا', 'إمّا', 'إن', 'إنَّ', 'إى', 'إياك', 'إياكم', 'إياكما', 'إياكن', 'إيانا', 'إياه', 'إياها', 'إياهم', 'إياهما', 'إياهن', 'إياي', 'إيهٍ', 'ئ', 'ا', 'ا?', 'ا?ى', 'االا', 'االتى', 'ابتدأ', 'ابين', 'اتخذ', 'اثر', 'اثنا', 'اثنان', 'اثني', 'اثنين', 'اجل', 'احد', 'اخرى', 'اخلولق', 'اذا', 'اربعة', 'اربعون', 'اربعين', 'ارتدّ', 'استحال', 'اصبح', 'اضحى', 'اطار', 'اعادة', 'اعلنت', 'اف', 'اكثر', 'اكد', 'الآن', 'الألاء', 'الألى', 'الا', 'الاخيرة', 'الان', 'الاول', 'الاولى', 'التى', 'التي', 'الثاني', 'الثانية', 'الحالي', 'الذاتي', 'الذى', 'الذي', 'الذين', 'السابق', 'الف', 'اللاتي', 'اللتان', 'اللتيا', 'اللتين', 'اللذان', 'اللذين', 'اللواتي', 'الماضي', 'المقبل', 'الوقت', 'الى', 'الي', 'اليه', 'اليها', 'اليوم', 'اما', 'امام', 'امس', 'امسى', 'ان', 'انبرى', 'انقلب', 'انه', 'انها', 'او', 'اول', 'اي', 'ايار', 'ايام', 'ايضا', 'ب', 'بؤسا', 'بإن', 'بئس', 'باء', 'بات', 'باسم', 'بان', 'بخٍ', 'بد', 'بدلا', 'برس', 'بسبب', 'بسّ', 'بشكل', 'بضع', 'بطآن', 'بعد', 'بعدا', 'بعض', 'بغتة', 'بل', 'بلى', 'بن', 'به', 'بها', 'بهذا', 'بيد', 'بين', 'بَسْ', 'بَلْهَ', 'ة', 'ت', 'تاء', 'تارة', 'تاسع', 'تانِ', 'تانِك', 'تبدّل', 'تجاه', 'تحت', 'تحوّل', 'تخذ', 'ترك', 'تسع', 'تسعة', 'تسعمئة', 'تسعمائة', 'تسعون', 'تسعين', 'تشرين', 'تعسا', 'تعلَّم', 'تفعلان', 'تفعلون', 'تفعلين', 'تكون', 'تلقاء', 'تلك', 'تم', 'تموز', 'تينك', 'تَيْنِ', 'تِه', 'تِي', 'ث', 'ثاء', 'ثالث', 'ثامن', 'ثان', 'ثاني', 'ثلاث', 'ثلاثاء', 'ثلاثة', 'ثلاثمئة', 'ثلاثمائة', 'ثلاثون', 'ثلاثين', 'ثم', 'ثمان', 'ثمانمئة', 'ثمانون', 'ثماني', 'ثمانية', 'ثمانين', 'ثمنمئة', 'ثمَّ', 'ثمّ', 'ثمّة', 'ج', 'جانفي', 'جدا', 'جعل', 'جلل', 'جمعة', 'جميع', 'جنيه', 'جوان', 'جويلية', 'جير', 'جيم', 'ح', 'حاء', 'حادي', 'حار', 'حاشا', 'حاليا', 'حاي', 'حبذا', 'حبيب', 'حتى', 'حجا', 'حدَث', 'حرى', 'حزيران', 'حسب', 'حقا', 'حمدا', 'حمو', 'حمٌ', 'حوالى', 'حول', 'حيث', 'حيثما', 'حين', 'حيَّ', 'حَذارِ', 'خ', 'خاء', 'خاصة', 'خال', 'خامس', 'خبَّر', 'خلا', 'خلافا', 'خلال', 'خلف', 'خمس', 'خمسة', 'خمسمئة', 'خمسمائة', 'خمسون', 'خمسين', 'خميس', 'د', 'دال', 'درهم', 'درى', 'دواليك', 'دولار', 'دون', 'دونك', 'ديسمبر', 'دينار', 'ذ', 'ذا', 'ذات', 'ذاك', 'ذال', 'ذانك', 'ذانِ', 'ذلك', 'ذهب', 'ذو', 'ذيت', 'ذينك', 'ذَيْنِ', 'ذِه', 'ذِي', 'ر', 'رأى', 'راء', 'رابع', 'راح', 'رجع', 'رزق', 'رويدك', 'ريال', 'ريث', 'رُبَّ', 'ز', 'زاي', 'زعم', 'زود', 'زيارة', 'س', 'ساء', 'سابع', 'سادس', 'سبت', 'سبتمبر', 'سبحان', 'سبع', 'سبعة', 'سبعمئة', 'سبعمائة', 'سبعون', 'سبعين', 'ست', 'ستة', 'ستكون', 'ستمئة', 'ستمائة', 'ستون', 'ستين', 'سحقا', 'سرا', 'سرعان', 'سقى', 'سمعا', 'سنة', 'سنتيم', 'سنوات', 'سوف', 'سوى', 'سين', 'ش', 'شباط', 'شبه', 'شتانَ', 'شخصا', 'شرع', 'شمال', 'شيكل', 'شين', 'شَتَّانَ', 'ص', 'صاد', 'صار', 'صباح', 'صبر', 'صبرا', 'صدقا', 'صراحة', 'صفر', 'صهٍ', 'صهْ', 'ض', 'ضاد', 'ضحوة', 'ضد', 'ضمن', 'ط', 'طاء', 'طاق', 'طالما', 'طرا', 'طفق', 'طَق', 'ظ', 'ظاء', 'ظل', 'ظلّ', 'ظنَّ', 'ع', 'عاد', 'عاشر', 'عام', 'عاما', 'عامة', 'عجبا', 'عدا', 'عدة', 'عدد', 'عدم', 'عدَّ', 'عسى', 'عشر', 'عشرة', 'عشرون', 'عشرين', 'عل', 'علق', 'علم', 'على', 'علي', 'عليك', 'عليه', 'عليها', 'علًّ', 'عن', 'عند', 'عندما', 'عنه', 'عنها', 'عوض', 'عيانا', 'عين', 'عَدَسْ', 'غ', 'غادر', 'غالبا', 'غدا', 'غداة', 'غير', 'غين', 'ـ', 'ف', 'فإن', 'فاء', 'فان', 'فانه', 'فبراير', 'فرادى', 'فضلا', 'فقد', 'فقط', 'فكان', 'فلان', 'فلس', 'فهو', 'فو', 'فوق', 'فى', 'في', 'فيفري', 'فيه', 'فيها', 'ق', 'قاطبة', 'قاف', 'قال', 'قام', 'قبل', 'قد', 'قرش', 'قطّ', 'قلما', 'قوة', 'ك', 'كأن', 'كأنّ', 'كأيّ', 'كأيّن', 'كاد', 'كاف', 'كان', 'كانت', 'كانون', 'كثيرا', 'كذا', 'كذلك', 'كرب', 'كسا', 'كل', 'كلتا', 'كلم', 'كلَّا', 'كلّما', 'كم', 'كما', 'كن', 'كى', 'كيت', 'كيف', 'كيفما', 'كِخ', 'ل', 'لأن', 'لا', 'لا سيما', 'لات', 'لازال', 'لاسيما', 'لام', 'لايزال', 'لبيك', 'لدن', 'لدى', 'لدي', 'لذلك', 'لعل', 'لعلَّ', 'لعمر', 'لقاء', 'لكن', 'لكنه', 'لكنَّ', 'للامم', 'لم', 'لما', 'لمّا', 'لن', 'له', 'لها', 'لهذا', 'لهم', 'لو', 'لوكالة', 'لولا', 'لوما', 'ليت', 'ليرة', 'ليس', 'ليسب', 'م', 'مئة', 'مئتان', 'ما', 'ما أفعله', 'ما انفك', 'ما برح', 'مائة', 'ماانفك', 'مابرح', 'مادام', 'ماذا', 'مارس', 'مازال', 'مافتئ', 'ماي', 'مايزال', 'مايو', 'متى', 'مثل', 'مذ', 'مرّة', 'مساء', 'مع', 'معاذ', 'معه', 'مقابل', 'مكانكم', 'مكانكما', 'مكانكنّ', 'مكانَك', 'مليار', 'مليم', 'مليون', 'مما', 'من', 'منذ', 'منه', 'منها', 'مه', 'مهما', 'ميم', 'ن', 'نا', 'نبَّا', 'نحن', 'نحو', 'نعم', 'نفس', 'نفسه', 'نهاية', 'نوفمبر', 'نون', 'نيسان', 'نيف', 'نَخْ', 'نَّ', 'ه', 'هؤلاء', 'ها', 'هاء', 'هاكَ', 'هبّ', 'هذا', 'هذه', 'هل', 'هللة', 'هلم', 'هلّا', 'هم', 'هما', 'همزة', 'هن', 'هنا', 'هناك', 'هنالك', 'هو', 'هي', 'هيا', 'هيهات', 'هيّا', 'هَؤلاء', 'هَاتانِ', 'هَاتَيْنِ', 'هَاتِه', 'هَاتِي', 'هَجْ', 'هَذا', 'هَذانِ', 'هَذَيْنِ', 'هَذِه', 'هَذِي', 'هَيْهات', 'و', 'و6', 'وأبو', 'وأن', 'وا', 'واحد', 'واضاف', 'واضافت', 'واكد', 'والتي', 'والذي', 'وان', 'واهاً', 'واو', 'واوضح', 'وبين', 'وثي', 'وجد', 'وراءَك', 'ورد', 'وعلى', 'وفي', 'وقال', 'وقالت', 'وقد', 'وقف', 'وكان', 'وكانت', 'ولا', 'ولايزال', 'ولكن', 'ولم', 'وله', 'وليس', 'ومع', 'ومن', 'وهب', 'وهذا', 'وهو', 'وهي', 'وَيْ', 'وُشْكَانَ', 'ى', 'ي', 'ياء', 'يفعلان', 'يفعلون', 'يكون', 'يلي', 'يمكن', 'يمين', 'ين', 'يناير', 'يوان', 'يورو', 'يوليو', 'يوم', 'يونيو', 'ّأيّان', '.', ',', ':', ';', '+', '=', '-', ')', '(', '}', '{', '`', '!', '@', '#', '$', '%', '^', '&', '*', '|', '"', "'", 'َ', 'ً', 'ُ', 'ٌ', '؟', ',', '،', '/', '?', '>', '<', '٬', 'ْ', '~', 'ِ', 'ٍ', 'ـ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '10.0', 'A', 'An', ']', '«', '»', 'لهؤلاء', 'لأنه', 'كله', '؛', 'إنه', 'Sue', 'وهى', 'ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'الي', 'بين', 'تحت', 'على', 'إلى', 'فوق', 'كان', 'فى', 'في', 'كل', 'لم', 'لن', 'له', 'من', 'هو', 'هي', 'قوة', 'كما', 'لها', 'منذ', 'وقد', 'ولا', 'لقاء', 'مقابل', 'هناك', 'وقال', 'وكان', 'وقالت', 'وكانت', 'فيه', 'لكن', 'وفي', 'ولم', 'ومن', 'وهو', 'وهي', 'يوم', 'فيها', 'منها', 'يكون', 'يمكن\tحيث', 'االا', 'اما', 'االتى', 'التي', 'اكثر', 'ايضا', 'الذى', 'الذي', 'الان', 'الذين', 'ابين', 'ذلك', 'دون', 'حول', 'حين', 'الى', 'انه', 'اول', 'انها', 'ف', 'و', 'و6', 'قد', 'لا', 'ما', 'مع', 'هذا', 'واحد', 'واضاف', 'واضافت', 'فان', 'قبل', 'قال', 'كان', 'لدى', 'نحو', 'هذه', 'وان', 'واكد', 'كانت', 'واوضح\t', 'ب', 'ا', 'أ', '،', 'عن', 'عند', 'عندما', 'على', 'عليه', 'عليها', 'تم', 'ضد', 'بعد', 'بعض', 'حتى', 'اذا', 'احد', 'بان', 'اجل', 'غير', 'بن', 'به', 'ثم', 'اف', 'ان', 'او', 'اي', 'بها', 'الي', 'بين', 'تحت', 'علي', 'اه', 'ال', 'ام', 'ان', 'اه', 'او', 'ال', 'الا', 'تي', 'في', 'قد', 'لقد', 'لا', 'ما', 'مع', 'هل', 'ذا', 'هذا', 'هذه', 'هذان', 'هاتين', 'هالاا', 'اللاتي', 'اللااي', 'اللواتي', 'تلك', 'انا', 'نحن', 'انت', 'انتما', 'انتم', 'انتن', 'هو', 'هي', 'هما', 'هم', 'هن', 'ما', 'من', 'اينما', 'متي', 'اين', 'ايان', 'لما', 'اذا', 'كلما', 'مهما', 'اذ', 'حيث', 'حيثما', 'اني', 'كيفما', 'كيف', 'هل', 'من', 'فيم', 'ما', 'اين', 'متي', 'اني', 'كم', 'ايان', 'بم', 'لم', 'مم', 'لماذا', 'ماذا', 'الا', 'عمن', 'علي', 'الي', 'في', 'من', 'عن', 'كي', 'و', 'مذ', 'منذ', 'حتي', 'خلا', 'عدا', 'حاشا', 'و', 'ثم', 'او', 'ام', 'بل', 'لكن', 'لا', 'حتي', 'يا', 'ايا', 'هيا', 'اي', 'لن', 'لم', 'لما', 'لا', 'ما', 'ان', 'ان', 'قد', 'لا', 'ان', 'اذ', 'لو', 'لولا', 'اما', 'لما', 'ها', 'يا', 'ان', 'ما', 'لو', 'كي', 'ان', 'كان', 'لكن', 'ليت', 'لعل', 'لا', 'عسي', '']