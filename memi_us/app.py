"""Memi US — practise your memory about the United States."""

import os

from memi_engine import MemiConfig, create_app

import memi_us.providers  # noqa: F401

config = MemiConfig(
    title="memi US",
    subtitle="practise your memory",
    favicon_color="#3C3B6E",
    sponsor_url="https://github.com/sponsors/filias",
    sponsor_text="sponsor",
    about_html="""
        <p>Memi US is a memory practice game about the United States.</p>
        <p>Pick a category, look at the image, and try to guess what it is
        before revealing the answer.</p>
        <p>States, capitals, NBA teams — there's always something to remember.</p>
    """,
    done_html="""
        <svg width="200" height="180" viewBox="0 0 80 72" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <clipPath id="heart-clip">
                    <path d="M40 68 C40 68 4 44 4 22 C4 10 14 2 24 2 C30 2 36 6 40 12 C44 6 50 2 56 2 C66 2 76 10 76 22 C76 44 40 68 40 68Z"/>
                </clipPath>
            </defs>
            <g clip-path="url(#heart-clip)">
                <rect x="0" y="0"  width="80" height="6"  fill="#B22234"/>
                <rect x="0" y="6"  width="80" height="6"  fill="#FFFFFF"/>
                <rect x="0" y="12" width="80" height="6"  fill="#B22234"/>
                <rect x="0" y="18" width="80" height="6"  fill="#FFFFFF"/>
                <rect x="0" y="24" width="80" height="6"  fill="#B22234"/>
                <rect x="0" y="30" width="80" height="6"  fill="#FFFFFF"/>
                <rect x="0" y="36" width="80" height="6"  fill="#B22234"/>
                <rect x="0" y="42" width="80" height="6"  fill="#FFFFFF"/>
                <rect x="0" y="48" width="80" height="6"  fill="#B22234"/>
                <rect x="0" y="54" width="80" height="6"  fill="#FFFFFF"/>
                <rect x="0" y="60" width="80" height="6"  fill="#B22234"/>
                <rect x="0" y="66" width="80" height="6"  fill="#FFFFFF"/>
                <rect x="0" y="0"  width="34" height="36" fill="#3C3B6E"/>
            </g>
            <path d="M40 68 C40 68 4 44 4 22 C4 10 14 2 24 2 C30 2 36 6 40 12 C44 6 50 2 56 2 C66 2 76 10 76 22 C76 44 40 68 40 68Z"
                  fill="none" stroke="var(--subtle, #888)" stroke-width="1.5"/>
        </svg>
    """,
)

instance_static = os.path.join(os.path.dirname(__file__), "..", "static")
app = create_app(config, instance_static=instance_static)

if __name__ == "__main__":
    app.run(debug=True, port=8088)
