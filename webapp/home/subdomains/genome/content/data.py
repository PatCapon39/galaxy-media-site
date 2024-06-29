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
        "title_md": "Import data to Galaxy",
        "description_md": "<p>Standard upload of data to Galaxy, from your computer or from the web.</p>",
        "button_link": '{{ galaxy_base_url }}/tool_runner?tool_id=upload1',
    },
    {
        "title_md": '<code>FastQC</code> - sequence quality reports',
        "description_md": '<p>Before using your sequencing data, it&apos;s important first ensure that the data quality is sufficient for your analysis.</p>',
        "inputs": [
            {'datatypes': ['fastq']},
            {'datatypes': ['bam']},
            {'datatypes': ['sam']},
        ],
        "button_link": "{{ galaxy_base_url }}/tool_runner?tool_id=toolshed.g2.bx.psu.edu%2Frepos%2Fdevteam%2Ffastqc%2Ffastqc",
    },
    {
        "title_md": '<code>FastP</code> - sequence quality reports, trimming & filtering',
        "description_md": '<p>Faster run than FastQC, this tool can also trim reads and filter by quality.</p>',
        "inputs": [
            {'datatypes': ['fastq']},
        ],
        "button_link": "{{ galaxy_base_url }}/tool_runner?tool_id=toolshed.g2.bx.psu.edu%2Frepos%2Fiuc%2Ffastp%2Ffastp",
    },
    {
        "title_md": '<code>NanoPlot</code> - visualize Oxford Nanopore data',
        "description_md": '<p>A plotting suite for Oxford Nanopore sequencing data and alignments.</p>',
        "inputs": [
            {'datatypes': ['fastq']},
            {'datatypes': ['fasta']},
            {'datatypes': ['vcf_bgzip']},
        ],
        "button_link": "{{ galaxy_base_url }}/tool_runner?tool_id=toolshed.g2.bx.psu.edu%2Frepos%2Fiuc%2Fnanoplot%2Fnanoplot",
    },
    {
        "title_md": '<code>GenomeScope</code> - estimate genome size',
        "description_md": '<p>A set of metrics and graphs to visualize genome size and complexity prior to assembly.</p>',
        "inputs": [
            {
                "datatypes": ["tabular"],
                "label": "Output from <code>Meryl</code> or <code>Jellyfish histo</code>",
            },
        ],
        "button_link": "{{ galaxy_base_url }}/tool_runner?tool_id=toolshed.g2.bx.psu.edu%2Frepos%2Fiuc%2Fgenomescope%2Fgenomescope",
    },
    {
        "title_md": '<code>Meryl</code> - count kmers',
        "description_md": '<p>Prepare kmer count histogram for input to GenomeScope.</p>',
        "inputs": [
            {'datatypes': ['fastq']},
            {'datatypes': ['fasta']},
        ],
        "button_link": "{{ galaxy_base_url }}/tool_runner?tool_id=toolshed.g2.bx.psu.edu%2Frepos%2Fiuc%2Fmeryl%2Fmeryl",
    },
]


workflows = [
    {
        "title_md": 'Data QC',
        "description_md": """
            <p>
              Report statistics from sequencing reads.
              <br>
              <br>
              Tools:
              <code>nanoplot</code>
              <code>fastqc</code>
              <code>multiqc</code>
            </p>""",
        "button_link": "{{ galaxy_base_url }}/workflows/trs_import?trs_server=workflowhub.eu&run_form=true&trs_id=222",
        "button_tip": "Import to Galaxy AU",
        "view_link": "https://workflowhub.eu/workflows/222",
        "view_tip": "View in WorkflowHub",
    },
    {
        "title_md": 'Kmer counting to estimate genome size',
        "description_md": """
            <p>
              Estimates genome size and heterozygosity based on counts of kmers.
              <br>
              <br>
              Tools:
              <code>meryl</code>
              <code>genomescope</code>
            </p>""",
        "button_link": "{{ galaxy_base_url }}/workflows/trs_import?trs_server=workflowhub.eu&run_form=true&trs_id=223",
        "button_tip": "Import to Galaxy AU",
        "view_link": "https://workflowhub.eu/workflows/223",
        "view_tip": "View in WorkflowHub",
    },
    {
        "title_md": 'Trim and filter reads',
        "description_md": """
            <p>
              Trims and filters raw sequence reads according to specified settings.
              <br>
              <br>
              Tools:
              <code>fastp</code>
            </p>""",
        "button_link": "{{ galaxy_base_url }}/workflows/trs_import?trs_server=workflowhub.eu&run_form=true&trs_id=224",
        "button_tip": "Import to Galaxy AU",
        "view_link": "https://workflowhub.eu/workflows/224",
        "view_tip": "View in WorkflowHub",
    },
]


help = [
    {
        "title_md": 'How can I import my genomics data?',
        "description_md": """
            <p>
              You can upload your data to Galaxy using the Upload tool from anywhere in Galaxy. Just look for the "Upload data" button at the top of the tool panel.
            </p>""",
        "button_link": "https://training.galaxyproject.org/training-material/topics/galaxy-interface/",
        "button_md": "More info",
    },
    {
        "title_md": 'How can I subsample my data?',
        "description_md": """
            <p>
              We recommend subsampling large data sets to test tools and workflows. A useful tool is <code>seqtk_seq</code>, setting the parameter at "Sample fraction of sequences"
            </p>""",
    },
    {
        "title_md": 'How can I import data from the BPA portal?',
        "description_md": """
            <p>
              BioPlatforms Australia allows data downloads via URL. Once you have generated one of these URLs in the BPA portal, you can import it into Galaxy using the "Fetch data" feature of the Upload tool.
            </p>""",
        "button_link": "https://australianbiocommons.github.io/how-to-guides/genome_assembly/hifi_assembly#in-depth-workflow-guide",
        "button_md": "More info",
    },
    {
        "title_md": 'Can I upload sensitive data?',
        "description_md": """
            <p>
              No, do not upload personal or sensitive, such as human health or clinical data.
              Please see our
              <a href="/about#data-privacy">Data Privacy</a>
              page for definitions of sensitive and health-related information.
            </p>
            <p>
              Please also make sure you have read our
              <a href="/about#terms-of-service">Terms of Service</a>,
              which covers hosting and analysis of research data.
            </p>""",
    },
    {
        "title_md": 'Is my data private?',
        "description_md": """
            <p>
              Please read our
              <a href="/about#data-privacy">Privacy Policy</a>
              for information on your personal data and any data that you upload.
            </p>""",
    },
    {
        "title_md": 'How can I increase my storage quota?',
        "description_md": """
            <p>
                Please submit a quota request if your Galaxy Australia account reaches its data storage limit. Requests are usually provisioned quickly if you provide a reasonable use case for your request.
            </p>""",
        "button_link": "/request/quota",
        "button_md": "Request",
    },
    {
        "title_md": 'Tutorial: Quality Control',
        "description_md": """
            <p>
              Quality control and data cleaning is an essential first step in any NGS analysis. This tutorial will show you how to use and interpret results from <code>FastQC</code>, <code>NanoPlot</code> and <code>PycoQC</code>.
            </p>""",
        "button_link": "https://training.galaxyproject.org/training-material/topics/sequence-analysis/tutorials/quality-control/tutorial.html",
        "button_md": "Tutorial",
    },
    {
        "title_md": 'Tutorial: introduction to Genomics and Galaxy',
        "description_md": """
            <p>
              This practical aims to familiarize you with the Galaxy user interface. It will teach you how to perform basic tasks such as importing data, running tools, working with histories, creating workflows, and sharing your work.
            </p>""",
        "button_link": "https://training.galaxyproject.org/training-material/topics/introduction/tutorials/galaxy-intro-strands/tutorial.html",
        "button_md": "Tutorial",
    },
    galaxy_au_support_item,
]
