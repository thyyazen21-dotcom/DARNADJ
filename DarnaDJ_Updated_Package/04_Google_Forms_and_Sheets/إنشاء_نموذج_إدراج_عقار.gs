/**
 * Darna DJ - creates a property-submission Google Form and linked response spreadsheet.
 * Run buildDarnaDjPropertyForm() from https://script.google.com while signed into the intended owner account.
 * This does not publish property listings. Review permissions and the created form before sharing it.
 * Google Forms file-upload items often require respondents to sign in; provide WhatsApp as an alternative.
 */
function buildDarnaDjPropertyForm() {
  const form = FormApp.create('Darna DJ | طلب إدراج عقار للإيجار');
  form.setDescription('هذا النموذج لاستلام طلب إدراج عقار في منصة السكن والإيجار في جيبوتي. إرسال الطلب لا يعني قبول العقار أو نشره. ستراجع الإدارة البيانات والسعر والتوافر وحق استخدام الصور قبل النشر. لا ترسل وثائق هوية حساسة عبر هذا النموذج.');
  form.setConfirmationMessage('تم استلام طلبك. هذا ليس تأكيدًا للنشر؛ ستتواصل الإدارة لمراجعة البيانات والتحقق من العقار.');
  form.setCollectEmail(false);
  form.setProgressBar(true);

  form.addSectionHeaderItem().setTitle('1) بيانات المالك أو الوكيل');
  form.addTextItem().setTitle('الاسم الكامل').setRequired(true);
  form.addMultipleChoiceItem().setTitle('الصفة').setChoiceValues(['مالك العقار','وكيل مفوض','مدير/ممثل شركة']).setRequired(true);
  form.addTextItem().setTitle('رقم واتساب مع مفتاح الدولة').setRequired(true);
  form.addTextItem().setTitle('البريد الإلكتروني (اختياري)').setRequired(false);
  form.addParagraphTextItem().setTitle('اشرح باختصار صلاحيتك لعرض العقار (لا ترفق وثائق حساسة هنا)').setRequired(true);

  form.addSectionHeaderItem().setTitle('2) بيانات العقار');
  form.addTextItem().setTitle('اسم/عنوان مختصر للعقار').setRequired(true);
  form.addListItem().setTitle('نوع العقار').setChoiceValues(['شقة','منزل','فيلا','غرفة','استوديو','سكن عائلي','مكتب','محل تجاري','أخرى']).setRequired(true);
  form.addTextItem().setTitle('المنطقة/الحي في جيبوتي').setRequired(true);
  form.addParagraphTextItem().setTitle('العنوان أو رابط الخريطة (إن وجد)').setRequired(false);
  form.addTextItem().setTitle('عدد غرف النوم').setRequired(true);
  form.addTextItem().setTitle('عدد الحمامات').setRequired(true);
  form.addTextItem().setTitle('السعة القصوى للنزلاء').setRequired(false);
  form.addCheckboxItem().setTitle('المرافق والخدمات المتوفرة').setChoiceValues(['تكييف','مطبخ','ماء','كهرباء','إنترنت','موقف سيارات','مصعد','غسالة','أثاث كامل','أخرى']).setRequired(false);
  form.addParagraphTextItem().setTitle('اشرح المرافق وما يشمله السعر وما لا يشمله').setRequired(true);

  form.addSectionHeaderItem().setTitle('3) السعر والتوافر');
  form.addTextItem().setTitle('السعر الأساسي بالدولار الأمريكي (أرقام فقط)').setRequired(true);
  form.addMultipleChoiceItem().setTitle('فترة السعر').setChoiceValues(['لليلة','للأسبوع','للشهر','لكامل مدة الإقامة','أخرى']).setRequired(true);
  form.addParagraphTextItem().setTitle('شروط الإيجار والوديعة والمصاريف الإضافية والإلغاء').setRequired(true);
  form.addMultipleChoiceItem().setTitle('حالة التوافر حسب علمك').setChoiceValues(['متاح حسب علمي','محجوز حاليًا','يحتاج إلى تأكيد']).setRequired(true);
  form.addTextItem().setTitle('تاريخ آخر تأكيد للسعر والتوافر (اختياري)').setRequired(false);

  form.addSectionHeaderItem().setTitle('4) الصور والإذن');
  form.addParagraphTextItem().setTitle('رابط مجلد صور أو اكتب أنك سترسل الصور عبر واتساب (اختياري)').setRequired(false);
  form.addParagraphTextItem().setTitle('رابط فيديو/جولة (اختياري)').setRequired(false);
  form.addCheckboxItem().setTitle('الإقرارات المطلوبة').setChoiceValues([
    'أقر بأن المعلومات صحيحة حسب علمي وأن لدي صلاحية عرض العقار.',
    'أملك أو أمتلك إذنًا لاستخدام الصور والمواد التي أرسلها.',
    'أوافق على مراجعة الإدارة للمعلومات والتواصل معي بشأن الطلب.'
  ]).setRequired(true);
  form.addParagraphTextItem().setTitle('ملاحظات إضافية').setRequired(false);

  const ss = SpreadsheetApp.create('Darna DJ | سجل طلبات إدراج العقارات');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());
  const result = { formEditUrl: form.getEditUrl(), formPublicUrl: form.getPublishedUrl(), responseSpreadsheetUrl: ss.getUrl() };
  Logger.log(JSON.stringify(result, null, 2));
  return result;
}
