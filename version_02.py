import streamlit as st

# ─── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Down the Hill · Restaurant & Bar",
    page_icon="🍽️",
    layout="wide"
)

# ─── CUSTOM CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
            
.stImage img {
    height: 350px !important;    
    object-fit: cover !important; 
    width: 350px !important;
}
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Raleway:wght@300;400;500;600&display=swap');

/* ── Root palette — Mediterranean coast ── */
:root {
    --teal:        #2A9D8F;
    --teal-dark:   #1F7A6E;
    --teal-light:  #A8D8D3;
    --sky:         #B8D9E8;
    --sky-light:   #E3F2F8;
    --sand:        #E8C97A;
    --sand-light:  #F5ECD4;
    --cream:       #FAF6EF;
    --white:       #FFFFFF;
    --navy:        #1C3A4A;
    --navy-light:  #2E5566;
    --muted:       #6B8F9E;
    --border:      rgba(42, 157, 143, 0.2);
    --border-soft: rgba(42, 157, 143, 0.1);
}

/* ── Global ── */
html, body, .stApp {
    background-color: var(--cream) !important;
    color: var(--navy);
    font-family: 'Raleway', sans-serif;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 0 !important; max-width: 1200px; }

/* ── Hero ── */
.hero {
    position: relative;
    background: linear-gradient(160deg, #0e2a38 0%, #1a4a5c 45%, #1d5a6a 100%);
    border-bottom: 3px solid var(--teal);
    padding: 5rem 2rem 4rem;
    text-align: center;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background:
        radial-gradient(ellipse 70% 50% at 50% 0%,   rgba(42,157,143,0.25) 0%, transparent 65%),
        radial-gradient(ellipse 50% 40% at 15% 100%,  rgba(168,216,211,0.1) 0%, transparent 60%),
        radial-gradient(ellipse 30% 30% at 85% 80%,   rgba(232,201,122,0.1) 0%, transparent 55%);
    pointer-events: none;
}
.hero-waves {
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 60px;
    background: var(--cream);
    clip-path: ellipse(55% 100% at 50% 100%);
}
.hero-eyebrow {
    font-family: 'Raleway', sans-serif;
    font-weight: 500;
    font-size: 0.75rem;
    letter-spacing: 6px;
    text-transform: uppercase;
    color: var(--teal-light);
    margin-bottom: 1.2rem;
    position: relative;
}
.hero-title {
    font-family: 'Cormorant Garamond', serif;
    font-weight: 300;
    font-size: clamp(3rem, 7vw, 5.5rem);
    color: rgba(255,255,255,0.65) !important;
    line-height: 1.05;
    margin: 0 0 0.3rem;
    letter-spacing: -1px;
    position: relative;
}
.hero-title em { font-style: italic; color: var(--teal-light); }
.hero-tagline {
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    font-size: 1.2rem;
    color: rgba(255,255,255,0.65);
    margin: 0.8rem 0 2.2rem;
    position: relative;
}
.hero-rating {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(168,216,211,0.3);
    border-radius: 2rem;
    padding: 0.4rem 1.2rem;
    font-size: 0.88rem;
    color: rgba(255,255,255,0.9);
    position: relative;
}
.stars { color: var(--sand); letter-spacing: 2px; }

/* ── Divider ── */
.divider { border: none; border-top: 1px solid var(--border); margin: 0; }

/* ── Section ── */
.section { padding: 3.5rem 1rem; }
.section-label {
    font-family: 'Raleway', sans-serif;
    font-weight: 600;
    font-size: 0.7rem;
    letter-spacing: 5px;
    text-transform: uppercase;
    color: var(--teal);
    margin-bottom: 0.6rem;
}
.section-title {
    font-family: 'Cormorant Garamond', serif;
    font-weight: 300;
    font-size: clamp(2rem, 4vw, 3rem);
    color: var(--navy);
    margin: 0 0 1.5rem;
    line-height: 1.1;
}
.section-title em { font-style: italic; color: var(--teal); }

/* ── About text ── */
.about-body {
    font-family: 'Raleway', sans-serif;
    font-weight: 300;
    font-size: 1.02rem;
    color: var(--navy-light);
    line-height: 1.9;
    margin-bottom: 0.8rem;
}

/* ── Event cards ── */
.event-grid { display: flex; gap: 1.2rem; flex-wrap: wrap; }
.event-card {
    flex: 1; min-width: 220px;
    background: var(--white);
    border: 1px solid var(--border);
    border-top: 3px solid var(--teal);
    border-radius: 4px;
    padding: 2rem 1.5rem;
    box-shadow: 0 2px 16px rgba(28,58,74,0.06);
    transition: box-shadow 0.3s, transform 0.3s;
}
.event-card:hover {
    box-shadow: 0 6px 28px rgba(42,157,143,0.15);
    transform: translateY(-3px);
}
.event-icon { font-size: 2rem; margin-bottom: 1rem; display: block; }
.event-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.5rem;
    color: var(--navy);
    margin-bottom: 0.5rem;
}
.event-desc {
    font-family: 'Raleway', sans-serif;
    font-weight: 300;
    font-size: 0.9rem;
    color: var(--muted);
    line-height: 1.7;
    margin-bottom: 1rem;
}
.event-tag {
    font-family: 'Raleway', sans-serif;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--teal);
}

/* ── Dish cards ── */
.dish-label {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.1rem;
    font-style: italic;
    color: var(--navy);
    text-align: center;
    margin-top: 0.75rem;
    margin-bottom: 0.25rem;
}

/* ── Price banner ── */
.price-banner {
    background: linear-gradient(135deg, var(--sky-light), rgba(168,216,211,0.2));
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 1.8rem 2rem;
    text-align: center;
    margin-top: 2rem;
}
.price-main {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.2rem;
    font-weight: 300;
    color: var(--navy);
}
.price-sub {
    font-family: 'Raleway', sans-serif;
    font-size: 0.85rem;
    color: var(--muted);
    margin-top: 0.3rem;
}

/* ── Highlights ── */
.badge-grid { display: flex; flex-wrap: wrap; gap: 0.6rem; margin-top: 0.5rem; }
.badge {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 2rem;
    padding: 0.35rem 0.9rem;
    font-size: 0.82rem;
    font-family: 'Raleway', sans-serif;
    font-weight: 400;
    color: var(--navy-light);
    white-space: nowrap;
    box-shadow: 0 1px 4px rgba(28,58,74,0.05);
}

/* ── Info card ── */
.info-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 2rem;
    
    box-shadow: 0 2px 12px rgba(28,58,74,0.05);
}
.info-label {
    font-family: 'Raleway', sans-serif;
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--teal);
    margin-bottom: 0.3rem;
}
.info-value {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.1rem;
    color: var(--navy);
    margin-bottom: 1.2rem;
    line-height: 1.6;
}
.info-value a { color: var(--teal-dark); text-decoration: none; }
.info-value a:hover { text-decoration: underline; }

/* ── Hours table ── */
.hours-row {
    display: flex;
    justify-content: space-between;
    padding: 0.4rem 0;
    border-bottom: 1px solid var(--border-soft);
    font-size: 0.9rem;
}
.hours-day  { color: var(--muted); font-family: 'Raleway', sans-serif; font-weight: 400; }
.hours-time { color: var(--navy);  font-family: 'Raleway', sans-serif; font-weight: 300; }

/* ── Social links ── */
.social-link {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    background: var(--sky-light);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 0.9rem 1.2rem;
    margin-bottom: 0.75rem;
    text-decoration: none;
    color: var(--navy);
    font-family: 'Raleway', sans-serif;
    font-size: 0.9rem;
    transition: border-color 0.3s, background 0.3s, transform 0.2s;
}
.social-link:hover {
    border-color: var(--teal);
    background: rgba(42,157,143,0.08);
    transform: translateX(4px);
}
.social-icon { font-size: 1.3rem; }
.social-text { font-weight: 500; color: var(--navy); }
.social-sub  { font-size: 0.75rem; color: var(--muted); }

/* ── Form inputs ── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: var(--white) !important;
    border: 1px solid var(--border) !important;
    border-radius: 4px !important;
    color: var(--navy) !important;
    font-family: 'Raleway', sans-serif !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: var(--teal) !important;
    box-shadow: 0 0 0 2px rgba(42,157,143,0.15) !important;
}
.stTextInput label, .stTextArea label {
    color: var(--muted) !important;
    font-family: 'Raleway', sans-serif !important;
    font-size: 0.78rem !important;
    font-weight: 600 !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
}

/* ── Button ── */
.stButton > button {
    background: var(--teal) !important;
    border: none !important;
    color: white !important;
    font-family: 'Raleway', sans-serif !important;
    font-size: 0.78rem !important;
    font-weight: 600 !important;
    letter-spacing: 2.5px !important;
    text-transform: uppercase !important;
    border-radius: 2px !important;
    padding: 0.65rem 2rem !important;
    transition: all 0.3s !important;
}
.stButton > button:hover {
    background: var(--teal-dark) !important;
    box-shadow: 0 4px 16px rgba(42,157,143,0.3) !important;
}

/* ── Link buttons ── */
.stLinkButton > a {
    background: transparent !important;
    border: 1px solid var(--border) !important;
    color: var(--teal-dark) !important;
    font-family: 'Raleway', sans-serif !important;
    font-size: 0.78rem !important;
    font-weight: 600 !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    border-radius: 2px !important;
    transition: all 0.3s !important;
}
.stLinkButton > a:hover {
    background: rgba(42,157,143,0.08) !important;
    border-color: var(--teal) !important;
    color: var(--teal) !important;
}

/* ── Expander ── */
.streamlit-expanderHeader {
    background: var(--sky-light) !important;
    border: 1px solid var(--border) !important;
    border-radius: 4px !important;
    color: var(--navy) !important;
    font-family: 'Raleway', sans-serif !important;
}

/* ── Images ── */
.stImage img { border-radius: 3px; }

/* ── Footer ── */
.site-footer {
    background: var(--navy);
    border-top: 3px solid var(--teal);
    padding: 3rem 2rem;
    text-align: center;
    margin-top: 3rem;
}
.footer-name {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.8rem;
    font-style: italic;
    color: var(--teal-light);
    margin-bottom: 0.5rem;
}
.footer-details {
    font-family: 'Raleway', sans-serif;
    font-size: 0.82rem;
    color: rgba(255,255,255,0.5);
    letter-spacing: 1px;
    line-height: 2.2;
}
.footer-details a { color: var(--teal-light); text-decoration: none; }
.footer-details a:hover { color: white; }
</style>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# HERO
# ════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero">
    <div class="hero-eyebrow">Bahçeli · Kyrenia · North Cyprus</div>
    <h1 class="hero-title">Down <em>the</em> Hill</h1>
    <p class="hero-tagline">Restaurant & Bar · Where the Mediterranean meets the hillside</p>
    <div style="display:flex; justify-content:center; gap:1rem; flex-wrap:wrap; margin-bottom:3rem; position:relative;">
        <span class="hero-rating">
            <span class="stars">★★★★★</span>
            <span>4.8 &nbsp;·&nbsp; 81 Google Reviews</span>
        </span>
        <span class="hero-rating">
            <span>🕐</span>
            <span>Open 7 Days &nbsp;·&nbsp; 11 AM – 11 PM</span>
        </span>
    </div>
    <div class="hero-waves"></div>
</div>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# ABOUT
# ════════════════════════════════════════════════════════════════════════════
st.markdown('<hr class="divider">', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    col_img, col_spacer, col_text = st.columns([1.1, 0.08, 1])

    with col_img:
        st.image(
            "https://i.postimg.cc/hhV1JNhn/unnamed-4.jpg",
            use_container_width=True
        )

    with col_text:
        st.markdown("""
        <div style="padding: 0.5rem 0 0 0.5rem;">
            <div class="section-label">Our Story</div>
            <h2 class="section-title">A Place to <em>Gather</em></h2>
            <p class="about-body">
                Perched in the rolling hills above Bahçeli, with the shimmering waters of Kyrenia 
                stretching out below, Down the Hill is where the island slows down and the good 
                things in life take centre stage.
            </p>
            <p class="about-body">
                From fresh sea bass pulled from the waters off Girne to a perfectly reduced 
                brandy sauce over fillet steak — our kitchen brings the finest Mediterranean 
                flavours to your table. Our bar is stocked with great wines, craft cocktails, 
                cold beers, and everything in between.
            </p>
            <p class="about-body">
                Locals, expats, and visitors from around the world share the same tables here. 
                Come for dinner — stay for the music.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        btn1, btn2 = st.columns([1, 1])
        with btn1:
            st.link_button("📞 Reserve a Table", "tel:+905338713320")
        with btn2:
            st.link_button("📍 Get Directions", "https://maps.app.goo.gl/o2JzSGKKD75J7ftF7")

    st.markdown('</div>', unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# EVENTS
# ════════════════════════════════════════════════════════════════════════════
st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown("""
<div class="section" style="background: linear-gradient(180deg, var(--sky-light) 0%, var(--cream) 100%); margin: 0; padding: 3.5rem 1rem;">
    <div style="text-align:center; margin-bottom:2.5rem;">
        <div class="section-label" style="text-align:center;">Events & Entertainment</div>
        <h2 class="section-title" style="text-align:center; margin-bottom:0.5rem;">The <em>Lively</em> Side</h2>
        <p style="color:var(--muted); font-family:'Raleway',sans-serif; font-size:0.92rem;">
            Follow our Facebook group to never miss an event
        </p>
    </div>
    <div class="event-grid">
        <div class="event-card">
            <span class="event-icon">🎸</span>
            <div class="event-title">Live Music Wednesday</div>
            <p class="event-desc">
                Every Wednesday evening we host live performances — from local singer-songwriters 
                to visiting acts. The perfect excuse to make midweek feel like a Friday.
            </p>
            <div class="event-tag">Every Wednesday</div>
        </div>
        <div class="event-card">
            <span class="event-icon">🪩</span>
            <div class="event-title">Disco Night</div>
            <p class="event-desc">
                When the sun goes down and the cocktails flow, we turn it up. Join our legendary 
                disco nights under the North Cyprus sky — dates announced in the Facebook group.
            </p>
            <div class="event-tag">Regular Events</div>
        </div>
        <div class="event-card">
            <span class="event-icon">👥</span>
            <div class="event-title">Community Nights</div>
            <p class="event-desc">
                A vibrant mix of locals, expats, and travellers makes every evening here unique. 
                Our Facebook community group is the best place to stay in the loop.
            </p>
            <div class="event-tag">
                <a href="https://www.facebook.com/groups/2626237331016967"
                   style="color:var(--teal); text-decoration:none;">
                    Join the Group →
                </a>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# MENU / DISHES
# ════════════════════════════════════════════════════════════════════════════
st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <div class="section-label">The Kitchen</div>
    <h2 class="section-title">Signature <em>Dishes</em></h2>
    <p style="color:var(--muted); font-family:'Raleway',sans-serif; font-size:0.9rem; margin-bottom:2rem; max-width:520px;">
        Our menu evolves with the seasons and the catch of the day. 
        Call ahead or ask your server for today's specials.
    </p>
</div>
""", unsafe_allow_html=True)

d1, d2, d3 = st.columns(3)
with d1:
    # Sea Bass photo link
    st.image(
        "https://i.postimg.cc/NyL7zVd5/unnamed.jpg",
        use_container_width=True
    )
    st.markdown('<div class="dish-label">Sea Bass</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:0.82rem;color:var(--muted);font-family:Raleway,sans-serif;">Fresh from the waters off Girne, simply grilled to perfection</p>', unsafe_allow_html=True)

with d2:
    #Fillet Steak photo link
    st.image(
        "https://i.postimg.cc/tssNrwSX/unnamed-2.jpg",
        use_container_width=True
    )
    st.markdown('<div class="dish-label">Fillet Steak in Pepper & Brandy</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:0.82rem;color:var(--muted);font-family:Raleway,sans-serif;">Tender fillet in a rich peppercorn and brandy reduction</p>', unsafe_allow_html=True)

with d3:
    # Gambas photo link
    st.image(
        "https://i.postimg.cc/xqGxHwhX/unnamed-3.jpg",
        use_container_width=True
    )
    st.markdown('<div class="dish-label">Gambas</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:0.82rem;color:var(--muted);font-family:Raleway,sans-serif;">Juicy prawns, Mediterranean style — a perennial favourite</p>', unsafe_allow_html=True)

st.markdown("""
<div class="price-banner">
    <div class="price-main">€15 – €40 per person</div>
    <div class="price-sub"> 550 – 1,450 TL per person</div>
</div>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# HIGHLIGHTS
# ════════════════════════════════════════════════════════════════════════════
st.markdown('<hr class="divider" style="margin-top:2.5rem;">', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <div class="section-label">Amenities & Atmosphere</div>
    <h2 class="section-title">What to <em>Expect</em></h2>
    <div class="badge-grid">
        <span class="badge">🍺 Great Beer Selection</span>
        <span class="badge">🍹 Great Cocktails</span>
        <span class="badge">🍷 Great Wine List</span>
        <span class="badge">☕ Great Coffee</span>
        <span class="badge">🫖 Great Tea</span>
        <span class="badge">🍰 Great Dessert</span>
        <span class="badge">🎵 Live Music</span>
        <span class="badge">🌿 Outdoor Seating</span>
        <span class="badge">🍽️ Dine-in & Takeout</span>
        <span class="badge">👨‍👩‍👧 Family Friendly</span>
        <span class="badge">♿ Wheelchair Accessible</span>
        <span class="badge">🅿️ Free Parking</span>
        <span class="badge">💳 Cards & NFC Pay</span>
        <span class="badge">📅 Reservations Recommended</span>
        <span class="badge">🌊 Great for Solo Dining</span>
    </div>
</div>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# LOCATION & CONTACT
# ════════════════════════════════════════════════════════════════════════════
st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown("""
<div class="section-label">Visit Us</div>
<h2 class="section-title">Find <em>Us</em></h2>
""", unsafe_allow_html=True)

contact_col, hours_col, social_col = st.columns(3)

with contact_col:
    st.markdown("""
    <div class="info-card">
        <div class="info-label">Address</div>
        <div class="info-value">Bahçeli, Kyrenia<br>North Cyprus<br>
            <a href="https://maps.app.goo.gl/o2JzSGKKD75J7ftF7">Open in Maps →</a>
        </div>
        <div class="info-label">Reservations</div>
        <div class="info-value">
            <a href="tel:+905338713320">+90 533 871 33 20</a><br>
            <span style="font-size:0.9rem; color:var(--muted); font-family:'Raleway',sans-serif;">Şaban Çetin</span>
        </div>
        <div class="info-label">Payment</div>
        <div class="info-value" style="font-size:0.95rem;">Cash · Credit & Debit Cards · NFC Mobile</div>
    </div>
    """, unsafe_allow_html=True)

with hours_col:
    st.markdown("""
    <div class="info-card">
        <div class="info-label" style="margin-bottom:1rem;">Opening Hours</div>
        <div class="hours-row"><span class="hours-day">Monday</span><span class="hours-time">11:00 AM – 11:00 PM</span></div>
        <div class="hours-row"><span class="hours-day">Tuesday</span><span class="hours-time">11:00 AM – 11:00 PM</span></div>
        <div class="hours-row"><span class="hours-day">Wednesday</span><span class="hours-time">11:00 AM – 11:00 PM </span></div>
        <div class="hours-row"><span class="hours-day">Thursday</span><span class="hours-time">11:00 AM – 11:00 PM</span></div>
        <div class="hours-row"><span class="hours-day">Friday</span><span class="hours-time">11:00 AM – 11:00 PM</span></div>
        <div class="hours-row"><span class="hours-day">Saturday</span><span class="hours-time">11:00 AM – 11:00 PM</span></div>
        <div class="hours-row"><span class="hours-day">Sunday</span><span class="hours-time">11:00 AM – 11:00 PM</span></div>
        
    </div>
    """, unsafe_allow_html=True)

with social_col:
    st.markdown("""
    <div class="info-card">
        <div class="info-label" style="margin-bottom:1rem;">Follow & Connect</div>
        <a class="social-link" href="https://www.instagram.com/downthehillrestaurant" target="_blank">
            <span class="social-icon">📸</span>
            <div>
                <div class="social-text">Instagram</div>
                <div class="social-sub">@downthehillrestaurant</div>
            </div>
        </a>
        <a class="social-link" href="https://www.facebook.com/groups/2626237331016967" target="_blank">
            <span class="social-icon">📘</span>
            <div>
                <div class="social-text">Facebook Community</div>
                <div class="social-sub">Events, updates & community</div>
            </div>
        </a>
        <a class="social-link" href="https://maps.app.goo.gl/o2JzSGKKD75J7ftF7" target="_blank">
            <span class="social-icon">🗺️</span>
            <div>
                <div class="social-text">Google Maps</div>
                <div class="social-sub">⭐ 4.8 · 81 reviews</div>
            </div>
        </a>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# CONTACT FORM
# ════════════════════════════════════════════════════════════════════════════
st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <div class="section-label">Get in Touch</div>
    <h2 class="section-title">Send Us a <em>Message</em></h2>
</div>
""", unsafe_allow_html=True)

with st.expander("Open contact form"):
    name  = st.text_input("Name")
    email = st.text_input("Email (optional)")
    msg   = st.text_area("Message", height=120)

    if st.button("Send Message"):
        if not name.strip() or not msg.strip():
            st.warning("Please fill in your name and message.")
        else:
            st.success(f"Thank you, {name}! We'll be in touch soon. See you down the hill. 🍽️")


# ════════════════════════════════════════════════════════════════════════════
# FOOTER
# ════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="site-footer">
    <div class="footer-name">Down the Hill</div>
    <div class="footer-details">
        Bahçeli, Kyrenia, North Cyprus &nbsp;·&nbsp; Open Daily 11 AM – 11 PM<br>
        <a href="tel:+905338713320">+90 533 871 33 20</a>
        &nbsp;·&nbsp;
        <a href="https://www.instagram.com/downthehillrestaurant">Instagram</a>
        &nbsp;·&nbsp;
        <a href="https://www.facebook.com/groups/2626237331016967">Facebook</a>
        &nbsp;·&nbsp;
        <a href="https://maps.app.goo.gl/o2JzSGKKD75J7ftF7">Google Maps</a>
    </div>
</div>
""", unsafe_allow_html=True)