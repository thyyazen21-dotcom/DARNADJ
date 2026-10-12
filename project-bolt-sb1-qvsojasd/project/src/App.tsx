import { useState, useEffect, useCallback } from 'react';
import {
  Home,
  Building2,
  House,
  Phone,
  DollarSign,
  Menu,
  Search,
  MapPin,
  BedDouble,
  Bath,
  Users,
  ChevronLeft,
  ChevronRight,
  MessageCircle,
  ShieldAlert,
  Info,
} from 'lucide-react';

type Property = {
  id: string;
  title: string;
  price: number;
  priceUnit: string;
  area: string;
  type: string;
  bedrooms: number;
  bathrooms: number;
  capacity: number;
  description: string;
  features: string[];
  images: string[];
  labels: string[];
  furnished: boolean;
};

const DEMO_PROPERTIES: Property[] = [
  {
    id: 'DJ-APT-0001',
    title: 'شقة مفروشة بإطلالة على البحر — حي الهرم',
    price: 800,
    priceUnit: 'شهريًا',
    area: 'جيبوتي المدينة',
    type: 'شقة',
    bedrooms: 2,
    bathrooms: 1,
    capacity: 4,
    description:
      'شقة حديثة مفروشة بالكامل في الطابق الثالث بإطلالة بانورامية على البحر. قريبة من الميناء والمراكز التجارية. تشمل الإقامة الماء والكهرباء والإنترنت.',
    features: ['تكييف', 'مطبخ مجهز', 'إنترنت', 'موقف سيارات', 'مصعد', 'غسالة'],
    images: [
      'https://images.pexels.com/photos/1571460/pexels-photo-1571460.jpeg?auto=compress&cs=tinysrgb&w=800',
      'https://images.pexels.com/photos/1648776/pexels-photo-1648776.jpeg?auto=compress&cs=tinysrgb&w=800',
      'https://images.pexels.com/photos/276724/pexels-photo-276724.jpeg?auto=compress&cs=tinysrgb&w=800',
    ],
    labels: ['شقة', 'جيبوتي-المدينة', 'مفروش', 'إطلالة-بحر'],
    furnished: true,
  },
  {
    id: 'DJ-VIL-0002',
    title: 'فيلا مستقلة بحديقة — منطقة الديك',
    price: 2500,
    priceUnit: 'شهريًا',
    area: 'جيبوتي المدينة',
    type: 'فيلا',
    bedrooms: 4,
    bathrooms: 3,
    capacity: 8,
    description:
      'فيلا واسعة مستقلة بحديقة خاصة وموقف لسيارتين. مناسبة للعائلات. تشمل الإقامة الماء والصيانة الأساسية. الكهرباء والإنترنت تحسب بشكل منفصل.',
    features: ['حديقة خاصة', 'موقف سيارات', 'تكييف مركزي', 'مطبخ مجهز', 'حراسة', 'مولد كهرباء'],
    images: [
      'https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg?auto=compress&cs=tinysrgb&w=800',
      'https://images.pexels.com/photos/1396122/pexels-photo-1396122.jpeg?auto=compress&cs=tinysrgb&w=800',
      'https://images.pexels.com/photos/259588/pexels-photo-259588.jpeg?auto=compress&cs=tinysrgb&w=800',
    ],
    labels: ['فيلا', 'جيبوتي-المدينة', 'حديقة', 'عائلي'],
    furnished: true,
  },
  {
    id: 'DJ-APT-0003',
    title: 'استوديو عصري قرب السفارة الفرنسية',
    price: 450,
    priceUnit: 'شهريًا',
    area: 'جيبوتي المدينة',
    type: 'استوديو',
    bedrooms: 1,
    bathrooms: 1,
    capacity: 2,
    description:
      'استوديو عصري مجهز بالكامل في موقع حيوي قرب السفارة الفرنسية. مناسب لشخص واحد أو زوجين. تشمل الإقامة جميع الخدمات.',
    features: ['تكييف', 'إنترنت', 'مطبخ مفتوح', 'مصعد', 'أثاث كامل'],
    images: [
      'https://images.pexels.com/photos/3935352/pexels-photo-3935352.jpeg?auto=compress&cs=tinysrgb&w=800',
      'https://images.pexels.com/photos/3935350/pexels-photo-3935350.jpeg?auto=compress&cs=tinysrgb&w=800',
    ],
    labels: ['استوديو', 'جيبوتي-المدينة', 'مفروش'],
    furnished: true,
  },
  {
    id: 'DJ-HOM-0004',
    title: 'منزل عائلي في تاجورة — 3 غرف',
    price: 600,
    priceUnit: 'شهريًا',
    area: 'تاجورة',
    type: 'منزل',
    bedrooms: 3,
    bathrooms: 2,
    capacity: 6,
    description:
      'منزل عائلي واسع في تاجورة بسعر مناسب. قريب من المدارس والأسواق. الماء والكهرباء غير مشمولين في السعر.',
    features: ['موقف سيارات', 'ساحة', 'مطبخ', 'تهوية جيدة'],
    images: [
      'https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg?auto=compress&cs=tinysrgb&w=800',
    ],
    labels: ['منزل', 'تاجورة', 'عائلي'],
    furnished: false,
  },
  {
    id: 'DJ-APT-0005',
    title: 'شقة حديثة في علي صبيح — وصول سهل',
    price: 350,
    priceUnit: 'شهريًا',
    area: 'علي صبيح',
    type: 'شقة',
    bedrooms: 1,
    bathrooms: 1,
    capacity: 3,
    description:
      'شقة اقتصادية حديثة في علي صبيح بمدخل مستقل. مناسبة للموظفين. تشمل الماء والكهرباء بحدود معقولة.',
    features: ['تكييف', 'مدخل مستقل', 'موقف سيارات', 'إنترنت'],
    images: [
      'https://images.pexels.com/photos/1571460/pexels-photo-1571460.jpeg?auto=compress&cs=tinysrgb&w=800',
    ],
    labels: ['شقة', 'علي-صبيح', 'اقتصادي'],
    furnished: true,
  },
  {
    id: 'DJ-VIL-0006',
    title: 'فيلا فاخرة بمسبح — الهرم',
    price: 4000,
    priceUnit: 'شهريًا',
    area: 'جيبوتي المدينة',
    type: 'فيلا',
    bedrooms: 5,
    bathrooms: 4,
    capacity: 10,
    description:
      'فيلا فاخرة بمسبح خاص وإطلالة بحرية مباشرة. تشمل جميع الخدمات والصيانة. مناسبة للمسؤولين ورؤساء البعثات الدبلوماسية.',
    features: ['مسبح خاص', 'إطلالة بحر', 'تكييف مركزي', 'حراسة 24/7', 'مولد', 'حديقة منسقة', 'موقف 4 سيارات'],
    images: [
      'https://images.pexels.com/photos/2462015/pexels-photo-2462015.jpeg?auto=compress&cs=tinysrgb&w=800',
      'https://images.pexels.com/photos/261101/pexels-photo-261101.jpeg?auto=compress&cs=tinysrgb&w=800',
      'https://images.pexels.com/photos/1396122/pexels-photo-1396122.jpeg?auto=compress&cs=tinysrgb&w=800',
    ],
    labels: ['فيلا', 'جيبوتي-المدينة', 'فاخر', 'مسبح', 'مفروش'],
    furnished: true,
  },
];

const WHATSAPP_NUMBER = '25377313443';
const AREA_OPTIONS = ['جيبوتي المدينة', 'علي صبيح', 'تاجورة', 'أوبوك', 'أرتابو', 'دخيل'];
const TYPE_OPTIONS = ['شقة', 'فيلا', 'منزل', 'استوديو', 'غرفة'];

type View = 'home' | 'detail' | 'about' | 'fees' | 'contact' | 'privacy' | 'terms' | 'cancellation' | 'complaints' | 'advertise';

export default function App() {
  const [view, setView] = useState<View>('home');
  const [selectedProperty, setSelectedProperty] = useState<Property | null>(null);
  const [searchQuery, setSearchQuery] = useState('');
  const [filterType, setFilterType] = useState('');
  const [filterArea, setFilterArea] = useState('');
  const [galleryIndex, setGalleryIndex] = useState(0);
  const [menuOpen, setMenuOpen] = useState(false);

  const filteredProperties = DEMO_PROPERTIES.filter((p) => {
    const matchesSearch =
      !searchQuery ||
      p.title.includes(searchQuery) ||
      p.area.includes(searchQuery) ||
      p.id.toLowerCase().includes(searchQuery.toLowerCase());
    const matchesType = !filterType || p.type === filterType;
    const matchesArea = !filterArea || p.area === filterArea;
    return matchesSearch && matchesType && matchesArea;
  });

  const openProperty = useCallback((prop: Property) => {
    setSelectedProperty(prop);
    setGalleryIndex(0);
    setView('detail');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }, []);

  const navigate = useCallback((v: View) => {
    setView(v);
    setMenuOpen(false);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }, []);

  const buildWhatsAppLink = (prop: Property) => {
    const msg = `السلام عليكم، أرغب بالاستفسار عن العقار ${prop.id} — ${prop.title}. السعر المعلن: ${prop.price} USD ${prop.priceUnit}. الرابط: [ضع-رابط-العقار]`;
    return `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(msg)}`;
  };

  const galleryNext = () => {
    if (!selectedProperty) return;
    setGalleryIndex((i) => (i + 1) % selectedProperty.images.length);
  };
  const galleryPrev = () => {
    if (!selectedProperty) return;
    setGalleryIndex((i) => (i === 0 ? selectedProperty.images.length - 1 : i - 1));
  };

  useEffect(() => {
    const handler = (e: KeyboardEvent) => {
      if (view !== 'detail' || !selectedProperty) return;
      if (e.key === 'ArrowLeft') galleryNext();
      if (e.key === 'ArrowRight') galleryPrev();
    };
    window.addEventListener('keydown', handler);
    return () => window.removeEventListener('keydown', handler);
  }, [view, selectedProperty]);

  return (
    <div className="min-h-screen bg-stone-50 flex flex-col" dir="rtl">
      {/* Header */}
      <header className="bg-teal-700 text-white sticky top-0 z-50 shadow-lg">
        <div className="max-w-6xl mx-auto px-4 py-3">
          <div className="flex items-center justify-between gap-4 flex-wrap">
            <button
              onClick={() => navigate('home')}
              className="flex items-center gap-2 text-xl font-bold text-white hover:opacity-90 transition-opacity"
            >
              <span className="w-9 h-9 bg-amber-600 rounded-lg flex items-center justify-center text-sm">D</span>
              دارنا DJ
            </button>

            <button
              className="md:hidden text-white p-1"
              onClick={() => setMenuOpen((o) => !o)}
              aria-label="القائمة"
            >
              <Menu size={24} />
            </button>

            <nav className={`flex gap-1 flex-wrap ${menuOpen ? 'flex w-full flex-col' : 'hidden md:flex'}`}>
              <NavBtn icon={<Home size={16} />} label="الرئيسية" onClick={() => navigate('home')} active={view === 'home'} />
              <NavBtn icon={<Building2 size={16} />} label="شقق" onClick={() => { setFilterType('شقة'); setFilterArea(''); navigate('home'); }} />
              <NavBtn icon={<House size={16} />} label="فلل" onClick={() => { setFilterType('فيلا'); setFilterArea(''); navigate('home'); }} />
              <NavBtn icon={<DollarSign size={16} />} label="الرسوم" onClick={() => navigate('fees')} active={view === 'fees'} />
              <NavBtn icon={<Phone size={16} />} label="تواصل" onClick={() => navigate('contact')} active={view === 'contact'} />
            </nav>

            <form
              className="hidden md:flex items-center bg-white/10 rounded-lg px-3 py-1.5 gap-2"
              onSubmit={(e) => {
                e.preventDefault();
                navigate('home');
              }}
            >
              <Search size={16} className="text-white/60" />
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="ابحث عن عقار..."
                className="bg-transparent text-white placeholder-white/60 text-sm outline-none w-40"
              />
            </form>
          </div>
        </div>
      </header>

      <main className="flex-1">
        {view === 'home' && (
          <>
            {/* Hero */}
            <section className="bg-gradient-to-br from-teal-700 to-teal-900 text-white py-16 px-4 text-center">
              <div className="max-w-3xl mx-auto">
                <h1 className="text-3xl md:text-4xl font-bold mb-3">منصة دارنا للإيجار في جيبوتي</h1>
                <p className="text-lg opacity-90 mb-6">
                  اعثر على شقق وفلل ومنازل للإيجار مع أسعار واضحة ورسوم شفافة وتواصل مباشر عبر واتساب
                </p>
                <div className="flex gap-2 justify-center flex-wrap bg-white/10 rounded-xl p-4">
                  <input
                    type="text"
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    placeholder="ابحث بكلمة..."
                    className="px-4 py-2.5 rounded-lg text-stone-900 text-sm outline-none w-48"
                  />
                  <select
                    value={filterType}
                    onChange={(e) => setFilterType(e.target.value)}
                    className="px-4 py-2.5 rounded-lg text-stone-900 text-sm outline-none"
                  >
                    <option value="">كل الأنواع</option>
                    {TYPE_OPTIONS.map((t) => (
                      <option key={t} value={t}>{t}</option>
                    ))}
                  </select>
                  <select
                    value={filterArea}
                    onChange={(e) => setFilterArea(e.target.value)}
                    className="px-4 py-2.5 rounded-lg text-stone-900 text-sm outline-none"
                  >
                    <option value="">كل المناطق</option>
                    {AREA_OPTIONS.map((a) => (
                      <option key={a} value={a}>{a}</option>
                    ))}
                  </select>
                  <button
                    onClick={() => navigate('home')}
                    className="bg-amber-600 hover:bg-amber-700 text-white px-6 py-2.5 rounded-lg font-semibold text-sm transition-colors"
                  >
                    تصفية
                  </button>
                </div>
              </div>
            </section>

            {/* Properties Grid */}
            <section className="max-w-6xl mx-auto px-4 py-10">
              <h2 className="text-2xl font-bold text-teal-800 mb-6 flex items-center gap-2">
                عقارات متاحة
                <span className="flex-1 h-0.5 bg-stone-200" />
              </h2>

              {filteredProperties.length === 0 ? (
                <div className="text-center py-20 text-stone-500">
                  <p className="text-lg">لا توجد عقارات مطابقة.</p>
                  <p className="text-sm mt-2">جرّب تغيير معايير البحث.</p>
                </div>
              ) : (
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
                  {filteredProperties.map((prop) => (
                    <PropertyCard key={prop.id} prop={prop} onClick={() => openProperty(prop)} />
                  ))}
                </div>
              )}

              {/* Filter chips */}
              <div className="mt-10">
                <h3 className="text-lg font-bold text-teal-800 mb-3">تصفية حسب النوع</h3>
                <div className="flex gap-2 flex-wrap mb-4">
                  {['شقة', 'فيلا', 'منزل', 'استوديو', 'غرفة'].map((t) => (
                    <button
                      key={t}
                      onClick={() => setFilterType(filterType === t ? '' : t)}
                      className={`px-4 py-1.5 rounded-full text-sm border transition-colors ${
                        filterType === t
                          ? 'bg-teal-700 text-white border-teal-700'
                          : 'bg-white text-stone-700 border-stone-300 hover:border-teal-500'
                      }`}
                    >
                      {t}
                    </button>
                  ))}
                </div>
                <h3 className="text-lg font-bold text-teal-800 mb-3">تصفية حسب المنطقة</h3>
                <div className="flex gap-2 flex-wrap">
                  {AREA_OPTIONS.map((a) => (
                    <button
                      key={a}
                      onClick={() => setFilterArea(filterArea === a ? '' : a)}
                      className={`px-4 py-1.5 rounded-full text-sm border transition-colors ${
                        filterArea === a
                          ? 'bg-teal-700 text-white border-teal-700'
                          : 'bg-white text-stone-700 border-stone-300 hover:border-teal-500'
                      }`}
                    >
                      {a}
                    </button>
                  ))}
                </div>
                <p className="text-xs text-stone-500 mt-3">
                  ملاحظة: هذه نسخة عرض تجريبية. التصفية في Blogger تعتمد على تصنيفات المدونة وقد لا تشمل كل العقارات في كل الصفحات.
                </p>
              </div>
            </section>
          </>
        )}

        {view === 'detail' && selectedProperty && (
          <section className="max-w-4xl mx-auto px-4 py-8">
            <button
              onClick={() => navigate('home')}
              className="text-teal-700 hover:text-teal-900 text-sm mb-4 flex items-center gap-1"
            >
              <ChevronRight size={16} /> العودة للقائمة
            </button>

            <div className="bg-white rounded-xl shadow-md p-6">
              <h1 className="text-2xl font-bold mb-2">{selectedProperty.title}</h1>

              {/* Meta badges */}
              <div className="flex flex-wrap gap-2 mb-3">
                {selectedProperty.labels.map((l) => (
                  <span key={l} className="bg-stone-100 border border-stone-200 px-3 py-1 rounded-md text-xs">
                    {l}
                  </span>
                ))}
              </div>

              <div className="text-2xl font-bold text-teal-700 mb-4">
                ${selectedProperty.price}
                <span className="text-sm font-normal text-stone-500"> {selectedProperty.priceUnit}</span>
              </div>

              {/* Fee disclosure */}
              <div className="bg-amber-50 border-r-4 border-amber-600 rounded-lg p-4 text-sm leading-relaxed mb-6">
                السعر المعروض هو السعر الأساسي للإقامة. رسوم خدمة المنصة 10% من إجمالي قيمة الإقامة تضاف بشكل منفصل.
                سيتم تقديم عرض سعر مكتوب مفصل يشمل: مبلغ الإقامة، رسوم الخدمة، أي رسوم أخرى، والإجمالي قبل تأكيد الحجز.
              </div>

              {/* Gallery */}
              {selectedProperty.images.length > 0 && (
                <div className="mb-6">
                  <div className="relative rounded-xl overflow-hidden bg-stone-200" style={{ height: '400px' }}>
                    <img
                      src={selectedProperty.images[galleryIndex]}
                      alt={`${selectedProperty.title} - صورة ${galleryIndex + 1}`}
                      className="w-full h-full object-cover"
                    />
                    {selectedProperty.images.length > 1 && (
                      <>
                        <button
                          onClick={galleryPrev}
                          className="absolute right-3 top-1/2 -translate-y-1/2 bg-black/50 hover:bg-black/70 text-white w-10 h-10 rounded-full flex items-center justify-center transition-colors"
                          aria-label="السابق"
                        >
                          <ChevronRight size={20} />
                        </button>
                        <button
                          onClick={galleryNext}
                          className="absolute left-3 top-1/2 -translate-y-1/2 bg-black/50 hover:bg-black/70 text-white w-10 h-10 rounded-full flex items-center justify-center transition-colors"
                          aria-label="التالي"
                        >
                          <ChevronLeft size={20} />
                        </button>
                      </>
                    )}
                  </div>
                  {selectedProperty.images.length > 1 && (
                    <div className="flex gap-2 mt-2 overflow-x-auto pb-1">
                      {selectedProperty.images.map((img, i) => (
                        <img
                          key={i}
                          src={img}
                          alt={`صورة مصغرة ${i + 1}`}
                          onClick={() => setGalleryIndex(i)}
                          className={`w-20 h-15 object-cover rounded-md cursor-pointer flex-shrink-0 border-2 transition-colors ${
                            i === galleryIndex ? 'border-teal-700' : 'border-transparent'
                          }`}
                          style={{ width: '80px', height: '60px' }}
                        />
                      ))}
                    </div>
                  )}
                </div>
              )}

              {/* Specs */}
              <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mb-6">
                <SpecCard icon={<BedDouble size={18} />} label="غرف النوم" value={String(selectedProperty.bedrooms)} />
                <SpecCard icon={<Bath size={18} />} label="الحمامات" value={String(selectedProperty.bathrooms)} />
                <SpecCard icon={<Users size={18} />} label="السعة" value={`${selectedProperty.capacity} أشخاص`} />
                <SpecCard icon={<MapPin size={18} />} label="المنطقة" value={selectedProperty.area} />
              </div>

              {/* Description */}
              <div className="mb-6">
                <h2 className="text-lg font-bold mb-2">وصف العقار</h2>
                <p className="leading-relaxed text-stone-700">{selectedProperty.description}</p>
              </div>

              {/* Features */}
              <div className="mb-6">
                <h2 className="text-lg font-bold mb-2">المواصفات والخدمات</h2>
                <ul className="grid grid-cols-2 gap-2">
                  {selectedProperty.features.map((f) => (
                    <li key={f} className="flex items-center gap-2 text-sm text-stone-700">
                      <span className="w-1.5 h-1.5 rounded-full bg-teal-600" />
                      {f}
                    </li>
                  ))}
                </ul>
              </div>

              {/* Property ID */}
              <p className="text-xs text-stone-500 mb-4">رقم العقار: {selectedProperty.id}</p>

              {/* Inquiry notice */}
              <div className="bg-yellow-50 border border-yellow-400 rounded-lg p-3 text-sm mb-4 flex items-start gap-2">
                <Info size={18} className="text-yellow-600 flex-shrink-0 mt-0.5" />
                <span>
                  الاستفسار عبر واتساب لا يؤكد التوافر ولا يشكل حجزًا. يجب على الإدارة التحقق من التوافر والسعر والشروط مع المالك، ثم إرسال عرض سعر مكتوب قبل تأكيد الحجز.
                </span>
              </div>

              {/* WhatsApp CTA */}
              <a
                href={buildWhatsAppLink(selectedProperty)}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 bg-green-500 hover:bg-green-600 text-white px-6 py-3 rounded-lg font-bold transition-colors"
              >
                <MessageCircle size={20} />
                استفسر عن هذا العقار عبر واتساب
              </a>
              <p className="text-xs text-stone-500 mt-2">
                رقم الواتساب: +253 77 31 34 43 — سيتم إدراج عنوان العقار ورقمه في رسالتك
              </p>
            </div>
          </section>
        )}

        {view === 'fees' && <FeesPage />}
        {view === 'contact' && <ContactPage />}
        {view === 'privacy' && <PrivacyPage />}
        {view === 'terms' && <TermsPage />}
        {view === 'cancellation' && <CancellationPage />}
        {view === 'complaints' && <ComplaintsPage />}
        {view === 'advertise' && <AdvertisePage />}
        {view === 'about' && <AboutPage />}
      </main>

      {/* Footer */}
      <footer className="bg-stone-900 text-white/70 mt-12">
        <div className="max-w-6xl mx-auto px-4 py-10">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-6">
            <div>
              <h4 className="text-white font-bold mb-3">دارنا DJ</h4>
              <p className="text-sm opacity-70">منصة إيجار العقارات في جيبوتي. أسعار واضحة ورسوم شفافة.</p>
            </div>
            <div>
              <h4 className="text-white font-bold mb-3">روابط</h4>
              <ul className="space-y-1.5">
                <li><button onClick={() => navigate('home')} className="hover:text-white text-sm">الرئيسية</button></li>
                <li><button onClick={() => navigate('contact')} className="hover:text-white text-sm">تواصل معنا</button></li>
                <li><button onClick={() => navigate('fees')} className="hover:text-white text-sm">سياسة الرسوم</button></li>
                <li><button onClick={() => navigate('terms')} className="hover:text-white text-sm">الشروط والأحكام</button></li>
              </ul>
            </div>
            <div>
              <h4 className="text-white font-bold mb-3">سياسات</h4>
              <ul className="space-y-1.5">
                <li><button onClick={() => navigate('privacy')} className="hover:text-white text-sm">الخصوصية</button></li>
                <li><button onClick={() => navigate('cancellation')} className="hover:text-white text-sm">الإلغاء والاسترداد</button></li>
                <li><button onClick={() => navigate('complaints')} className="hover:text-white text-sm">تقديم شكوى</button></li>
                <li><button onClick={() => navigate('advertise')} className="hover:text-white text-sm">الإعلان</button></li>
              </ul>
            </div>
            <div>
              <h4 className="text-white font-bold mb-3">تواصل</h4>
              <p className="text-sm">واتساب: <a href={`https://wa.me/${WHATSAPP_NUMBER}`} className="text-green-400 font-semibold" target="_blank" rel="noopener noreferrer">+253 77 31 34 43</a></p>
              <p className="text-sm mt-2 opacity-60">الاستفسار لا يؤكد التوافر أو الحجز</p>
            </div>
          </div>
          <div className="border-t border-white/15 pt-4 text-center text-xs opacity-50">
            <p>© دارنا DJ — جميع الحقوق محفوظة. الاسم ترشيحي مؤقت ولم يتم تأكيد تسجيله.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}

function NavBtn({ icon, label, onClick, active }: { icon: React.ReactNode; label: string; onClick: () => void; active?: boolean }) {
  return (
    <button
      onClick={onClick}
      className={`px-3.5 py-2 rounded-md text-sm font-semibold transition-colors flex items-center gap-1.5 ${
        active ? 'bg-white/15 text-white' : 'text-white/90 hover:bg-white/10'
      }`}
    >
      {icon}
      {label}
    </button>
  );
}

function PropertyCard({ prop, onClick }: { prop: Property; onClick: () => void }) {
  return (
    <article
      className="bg-white rounded-xl overflow-hidden shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-200 flex flex-col cursor-pointer"
      onClick={onClick}
    >
      <div className="w-full h-48 bg-stone-200 overflow-hidden">
        {prop.images[0] ? (
          <img src={prop.images[0]} alt={prop.title} className="w-full h-full object-cover" loading="lazy" />
        ) : (
          <div className="w-full h-full flex items-center justify-center text-stone-400 text-sm">لا توجد صورة</div>
        )}
      </div>
      <div className="p-4 flex flex-col flex-1">
        <h3 className="text-base font-bold mb-1.5 text-stone-900">{prop.title}</h3>
        <div className="flex flex-wrap gap-1.5 mb-2">
          <span className="bg-stone-100 px-2 py-0.5 rounded text-xs text-stone-600">{prop.type}</span>
          <span className="bg-stone-100 px-2 py-0.5 rounded text-xs text-stone-600">{prop.area}</span>
          <span className="bg-stone-100 px-2 py-0.5 rounded text-xs text-stone-600">{prop.bedrooms} غرف</span>
        </div>
        <div className="text-xl font-bold text-teal-700 mb-1">
          ${prop.price}
          <span className="text-xs font-normal text-stone-500"> {prop.priceUnit}</span>
        </div>
        <div className="text-xs text-amber-800 bg-amber-50 border border-amber-200 rounded px-2 py-1 mb-3">
          السعر الأساسي. رسوم خدمة 10% تضاف منفصلاً.
        </div>
        <button className="mt-auto bg-teal-700 hover:bg-teal-800 text-white text-center py-2.5 rounded-lg font-semibold text-sm transition-colors">
          عرض التفاصيل
        </button>
      </div>
    </article>
  );
}

function SpecCard({ icon, label, value }: { icon: React.ReactNode; label: string; value: string }) {
  return (
    <div className="bg-stone-50 border border-stone-200 rounded-lg p-3 text-center">
      <div className="text-teal-700 mx-auto mb-1 flex justify-center">{icon}</div>
      <div className="text-xs text-stone-500">{label}</div>
      <div className="text-sm font-semibold">{value}</div>
    </div>
  );
}

function PageShell({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <section className="max-w-3xl mx-auto px-4 py-8">
      <div className="bg-white rounded-xl shadow-md p-6 md:p-8">
        <h1 className="text-2xl font-bold text-teal-800 mb-4">{title}</h1>
        <div className="prose prose-stone max-w-none text-stone-700 leading-relaxed" dir="rtl">
          {children}
        </div>
      </div>
    </section>
  );
}

function FeesPage() {
  return (
    <PageShell title="سياسة الرسوم والعمولات">
      <h2 className="text-lg font-bold mb-2">عمولة المالك</h2>
      <ul className="space-y-2 mb-4">
        <li>• عمولة مقترحة: 10% من إجمالي قيمة الإقامة المتفق عليها لكامل مدة الإقامة.</li>
        <li>• يجب توقيع اتفاق كتابي للوساطة/العمولة مع المالك أو الوكيل المفوض قبل النشر.</li>
        <li>• لا يمكن اعتماد العقار للنشر قبل تسجيل الاتفاقية الموقعة.</li>
        <li>• أي تغيير في التواريخ أو المدة أو السعر يجب أن ينعكس على عرض السعر والسجل.</li>
      </ul>
      <h2 className="text-lg font-bold mb-2">رسوم خدمة المستأجر</h2>
      <ul className="space-y-2 mb-4">
        <li>• رسوم خدمة مقترحة: 10% من إجمالي قيمة الإقامة لكامل مدة الإقامة.</li>
        <li>• رسوم منفصلة عن السعر المعلن. لا يتم إخفاؤها في السعر.</li>
        <li>• يتم عرضها بوضوح في صفحة العقار قرب السعر.</li>
        <li>• قبل تأكيد الحجز، يُرسل عرض سعر مكتوب مفصل يشمل جميع البنود.</li>
      </ul>
      <h2 className="text-lg font-bold mb-2">مثال توضيحي</h2>
      <p className="mb-2">بالنسبة لإقامة بقيمة 1,000 دولار أمريكي:</p>
      <ul className="space-y-1 mb-4">
        <li>• قيمة الإقامة: 1,000 دولار</li>
        <li>• عمولة المالك (10%): 100 دولار</li>
        <li>• رسوم خدمة المستأجر (10%): 100 دولار</li>
        <li>• إجمالي إيراد المنصة المحتمل: 200 دولار (قبل المصاريف والضرائب)</li>
        <li>• إذا دفع المستأجر مباشرة للمالك: إجمالي ما يدفعه المستأجر = 1,100 دولار</li>
      </ul>
      <div className="bg-amber-50 border-r-4 border-amber-600 p-3 rounded text-sm">
        <ShieldAlert size={18} className="inline ml-1 text-amber-600" />
        النسب المقترحة ليست ملزمة قانونيًا. يجب مراجعة صياغة العقود وتحصيل الرسوم قانونيًا في جيبوتي قبل الإطلاق التجاري.
      </div>
    </PageShell>
  );
}

function ContactPage() {
  return (
    <PageShell title="تواصل معنا">
      <p className="mb-4">يمكنك التواصل معنا عبر القنوات التالية للاستفسار عن عقار أو إدراج عقارك أو الإعلان على المنصة.</p>
      <div className="space-y-3 mb-4">
        <div className="bg-stone-50 border border-stone-200 rounded-lg p-4">
          <div className="font-semibold text-teal-700 mb-1">واتساب</div>
          <a href="https://wa.me/25377313443" className="text-green-600 font-bold" target="_blank" rel="noopener noreferrer">+253 77 31 34 43</a>
        </div>
        <div className="bg-stone-50 border border-stone-200 rounded-lg p-4">
          <div className="font-semibold text-teal-700 mb-1">إدراج عقار</div>
          <p className="text-sm">لإدراج عقارك، يرجى ملء نموذج Google Forms (بعد إنشائه) أو التواصل عبر واتساب.</p>
        </div>
        <div className="bg-yellow-50 border border-yellow-400 rounded-lg p-3 text-sm flex items-start gap-2">
          <Info size={18} className="text-yellow-600 flex-shrink-0 mt-0.5" />
          <span>الاستفسار عبر واتساب لا يؤكد التوافر ولا يشكل حجزًا مؤكدًا.</span>
        </div>
      </div>
    </PageShell>
  );
}

function PrivacyPage() {
  return (
    <PageShell title="سياسة الخصوصية">
      <div className="space-y-3 text-sm">
        <p>تلتزم منصة دارنا DJ بحماية خصوصية زوارها ومستخدميها.</p>
        <h2 className="text-lg font-bold">البيانات التي نجمعها</h2>
        <ul className="space-y-1">
          <li>• البيانات التي تقدمها طوعًا عبر نماذج التواصل أو Google Forms (الاسم، رقم الاتصال، البريد الإلكتروني).</li>
          <li>• لا نطلب وثائق هوية حساسة عبر النماذج الإلكترونية.</li>
        </ul>
        <h2 className="text-lg font-bold">استخدام البيانات</h2>
        <p>تُستخدم البيانات فقط لمراجعة طلبات الإدراج والتواصل بشأن العقارات. لا تُباع أو تُشارك مع أطراف ثالثة لأغراض تسويقية.</p>
        <h2 className="text-lg font-bold">ملفات تعريف الارتباط</h2>
        <p>يستخدم Blogger ملفات تعريف ارتباط أساسية للتشغيل. راجع سياسة Google للخصوصية للمزيد.</p>
      </div>
    </PageShell>
  );
}

function TermsPage() {
  return (
    <PageShell title="الشروط والأحكام">
      <div className="space-y-3 text-sm">
        <p>باستخدامك منصة دارنا DJ فإنك توافق على الشروط التالية:</p>
        <h2 className="text-lg font-bold">طبيعة المنصة</h2>
        <p>دارنا DJ منصة وسيطة لعرض العقارات للإيجار. لا تملك العقارات ولا تتحكم بتوافرها الفعلي. الإدارة تتحقق من التوافر والسعر مع المالك قبل الإرسال.</p>
        <h2 className="text-lg font-bold">الأسعار والرسوم</h2>
        <p>السعر المعروض هو السعر الأساسي. رسوم خدمة 10% تضاف بشكل منفصل. عرض السعر المكتوب هو المرجع الملزم قبل الحجز.</p>
        <h2 className="text-lg font-bold">مسؤولية المستخدم</h2>
        <p>الاستفسار عبر واتساب لا يشكل حجزًا مؤكدًا. المستأجر ملزم بمراجعة عرض السعر المكتوب والموافقة عليه قبل الالتزام.</p>
      </div>
    </PageShell>
  );
}

function CancellationPage() {
  return (
    <PageShell title="سياسة الإلغاء والاسترداد">
      <div className="space-y-3 text-sm">
        <h2 className="text-lg font-bold">الإلغاء قبل التأكيد</h2>
        <p>يمكنك إلغاء طلبك في أي مرحلة قبل قبول عرض السعر المكتوب دون أي التزام مالي.</p>
        <h2 className="text-lg font-bold">الإلغاء بعد التأكيد</h2>
        <p>شروط الإلغاء والاسترداد بعد التأكيد تخع لشروط العقد الموقّع بين المالك والمستأجر. تُحدد شروط الإلغاء في عرض السعر واتفاقية المالك.</p>
        <h2 className="text-lg font-bold">النزاعات</h2>
        <p>في حال وجود نزاع، يُرجع أولاً لشروط العقد. تتوسط الإدارة لتسهيل الحل دون تحمل مسؤولية قانونية عن العقود بين الأطراف.</p>
      </div>
    </PageShell>
  );
}

function ComplaintsPage() {
  return (
    <PageShell title="تقديم شكوى">
      <p className="mb-4">إذا كانت لديك شكوى بشأن عقار أو خدمة، يرجى التواصل عبر واتساب مع ذكر رقم العقار وتفاصيل الشكوى.</p>
      <a href="https://wa.me/25377313443" className="inline-flex items-center gap-2 bg-green-500 hover:bg-green-600 text-white px-5 py-2.5 rounded-lg font-bold transition-colors" target="_blank" rel="noopener noreferrer">
        <MessageCircle size={18} />
        تقديم شكوى عبر واتساب
      </a>
      <p className="text-xs text-stone-500 mt-3">سيتم مراجعة الشكوى والرد خلال 48 ساعة عملية.</p>
    </PageShell>
  );
}

function AdvertisePage() {
  return (
    <PageShell title="الإعلان على المنصة">
      <p className="mb-4">تتوفر مساحات إعلانية قابلة للتعديل في الشريط الجانبي والصفحات الرئيسية. للتفاصير والأسعار، تواصل عبر واتساب.</p>
      <a href="https://wa.me/25377313443" className="inline-flex items-center gap-2 bg-green-500 hover:bg-green-600 text-white px-5 py-2.5 rounded-lg font-bold transition-colors" target="_blank" rel="noopener noreferrer">
        <MessageCircle size={18} />
        استفسر عن الإعلان
      </a>
    </PageShell>
  );
}

function AboutPage() {
  return (
    <PageShell title="حول دارنا DJ">
      <p className="mb-4">دارنا DJ منصة وسيطة لعرض عقارات الإيجار في جيبوتي. تتيح للمالكين والوكلاء نشر عقاراتهم وللمستأجرين البحث والتواصل المباشر.</p>
      <p className="text-sm text-stone-600">الاسم ترشيحي مؤقت ولم يتم تأكيد تسجيل العلامة أو النطاق.</p>
    </PageShell>
  );
}
