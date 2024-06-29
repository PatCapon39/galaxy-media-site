"""Content for data section - tools, workflows and help tabs."""

galaxy_au_support_item = {
    "title_md": 'Galaxy Australia support',
    "description_md": """<p>
            Any user of Galaxy Australia can request support through an
            online form.
        </p>""",
    "button_link": "/request/support",
    "button_md": "Request support",
}

tools = [
    # {   # Accordion item schema:
    #     "title_md": '',
    #     "description_md": """""",
    #     "inputs": [
    #         {
    #             'datatypes': [''],
    #             'label': '',
    #         },
    #     ],
    #     "button_link": "",
    #     "button_md": "",
    #     "button_tip": "",
    #     "view_link": "",
    #     "view_md": "",
    #     "view_tip": "",
    # },
    {
        "title_md": '<code>MaxQuant</code>',
        "description_md": '<p>MaxQuant is a quantitative proteomics software package designed for analyzing large mass-spectrometric data sets.</p>',
        "inputs": [
            {
                'datatypes': [
                    'thermo.raw',
                    'mzML',
                    'mzXML',
                ],
                'label': 'MS spectra (input file)',
            },
            {
                'datatypes': ['tabular'],
                'label': 'Experimental design template',
            },
        ],
        "button_link": "https://usegalaxy.org.au/root?tool_id=toolshed.g2.bx.psu.edu/repos/galaxyp/maxquant/maxquant/",
    },
    {
        "title_md": '<code>MSstats</code>',
        "description_md": '<p>Statistical relative protein significance analysis in DDA, SRM and DIA Mass Spectrometry.</p>',
        "inputs": [
            {
                'datatypes': ['tabular', 'csv'],
                'label': 'Either the 10-column MSstats format or the outputs of spectral processing tools such as MaxQuant, OpenSWATH.',
            }
        ],
        "button_link": "https://usegalaxy.org.au/root?tool_id=toolshed.g2.bx.psu.edu/repos/galaxyp/msstats/msstats/",
    },
    {
        "title_md": '<code>LFQ Analyst</code>',
        "description_md": '<p>Analyze and Visualize Label-Free Proteomics output from MaxQuant.</p>',
        "inputs": [
            {
                'datatypes': ['txt'],
                'label': 'Protein groups (MaxQuant output)',
            },
            {
                'datatypes': ['txt'],
                'label': 'Experimental Design Matrix (MaxQuant output)',
            }
        ],
        "button_link": "https://usegalaxy.org.au/root?tool_id=interactive_tool_lfqanalyst_2",
    }
]


help = [
    {
        "title_md": 'LFQ-Analyst: Manual',
        "description_md": """
            <p>
              A detailed user manual for LFQ-Analyst.
            </p>""",
        "button_link": "https://analyst-suite.monash-proteomics.cloud.edu.au/apps/lfq-analyst/LFQ-Analyst_manual.pdf",
        "button_md": "Manual",
    },
    {
        "title_md": 'MaxQuant and MSstats for the analysis of label-free data',
        "description_md": """
        <p>
          Learn how to use MaxQuant and MSstats for the analysis of label-free shotgun (DDA) data.
        </p>""",
        "button_link": "https://training.galaxyproject.org/training-material/topics/proteomics/tutorials/maxquant-msstats-dda-lfq/tutorial.html",
        "button_md": "Tutorial",
    },
    galaxy_au_support_item,
]

