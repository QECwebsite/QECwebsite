from pathlib import Path
import re
path = Path('index.html')
text = path.read_text()
replacements = {
    'Communication': '''            <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 14h20a6 6 0 0 1 6 6v6a6 6 0 0 1-6 6h-7l-7 7v-7h-6a6 6 0 0 1-6-6v-6a6 6 0 0 1 6-6z" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M20 22h12M20 28h8" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M30 8h8a4 4 0 0 1 4 4v4a4 4 0 0 1-4 4h-1.5L34 23v-3h-2a4 4 0 0 1-4-4v-4a4 4 0 0 1 4-4z" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" />
            </svg>''',
    'Debate': '''            <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
              <path d="M24 10v26" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
              <path d="M14 16h20" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
              <path d="M16 16v8" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
              <path d="M32 16v8" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
              <path d="M8 24h16c0 4.4-3.6 8-8 8s-8-3.6-8-8z" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round" />
              <path d="M24 24h16c0 4.4-3.6 8-8 8s-8-3.6-8-8z" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round" />
              <path d="M18 38h12" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
            </svg>''',
    'Consulting': '''            <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
              <rect x="10" y="12" width="28" height="20" rx="4" ry="4" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M24 32v8" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
              <path d="M18 40h12" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
              <path d="M16 28l6-8 6 6 6-10" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" />
            </svg>''',
    'Bio-Engineering': '''            <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
              <path d="M18 10c6 4 6 12 0 16s-6 12 0 16" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
              <path d="M30 10c-6 4-6 12 0 16s6 12 0 16" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
              <path d="M18 18h12" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
              <path d="M18 26h12" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
              <path d="M18 34h12" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
              <path d="M32 6c4 2 6 6 4 10-4 0-8-4-4-10z" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" />
            </svg>''',
    'Innovation': '''            <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
              <path d="M24 8a12 12 0 0 1 12 12c0 5-2.4 8.4-5 11l-1 1.2V36H18v-3.8l-1-1.2c-2.6-2.6-5-6-5-11A12 12 0 0 1 24 8z" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M18 40h12" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
              <path d="M20 44h8" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
              <path d="M24 2v4" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
              <path d="M12 12l-3-3" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
              <path d="M36 12l3-3" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
            </svg>''',
    'Re-Engineering': '''            <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
              <circle cx="24" cy="24" r="8" fill="none" stroke="currentColor" stroke-width="2.4" />
              <path d="M24 16v4" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
              <path d="M24 28v4" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
              <path d="M16 24h4" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
              <path d="M28 24h4" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
              <path d="M16 16A12 12 0 0 1 36 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
              <path d="M36 24l-2-6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
              <path d="M36 24l6-2" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
              <path d="M32 32A12 12 0 0 1 12 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
              <path d="M12 24l2 6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
              <path d="M12 24l-6 2" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
            </svg>''',
    'Design (Junior & Senior)': '''            <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 34V12h22L12 34z" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M18 20h6v6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M28 18l12 12-6 6-12-12z" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M38 30l4 4" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" />
            </svg>''',
    'Programming': '''            <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
              <path d="M20 16l-8 8 8 8" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M28 16l8 8-8 8" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M24 14l-4 20" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" />
            </svg>'''
}

for name, svg in replacements.items():
    pattern = fr'(<span class="category-icon" aria-hidden="true">\s*)(<svg.*?</svg>)(\s*</span>\s*(?=(?:.|\n)*?<h3>{re.escape(name)}</h3>))'
    text, count = re.subn(pattern, r'\1' + svg + r'\3', text, count=1, flags=re.DOTALL)
    if count != 1:
        raise SystemExit(f'Replacement failed for {name}')

path.write_text(text)
