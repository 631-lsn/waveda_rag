---
title: "Symbol and Footprint Database"
merged_source: "current_user_dropbox"
source_relative_path: "SFgen_prcv.pdf"
original_path: "D:\RAGGG\knowledge_sources\user_dropbox\SFgen_prcv.pdf"
content_kind: "pdf_as_markdown"
merged_at: "2026-07-07"
---

# Symbol and Footprint Database

第 1 页
Symbol and Footprint Database
for Electronic Components
by Agentic Recognition and Generation
Yichen Shi1,2* , Yuzhi Liu3* , Zhuofu Tao3, Li Huang 1,2, Yuhao Gao3,
Ting-Jung Lin1** , and Lei He 1**
1 Ningbo Institute of Digital Twin, Eastern Institute of Technology, Ningbo, China
tlin@idt.eitech.edu.cn, lhe@eitech.edu.cn
2 Shanghai Jiao Tong University, Shanghai, China
shiyichen@sjtu.edu.cn
3 BTD Technology, Ningbo, China
yuzhi.liu@btd.tech
Abstract. A rich and recognizable component library is the corner-
stone of printed circuit board (PCB) design and generation. Tradition-
ally, engineers manually create symbols and footprints and design PCB
schematics, which is time-consuming and error-prone. Leveraging multi-
modal large language models (MLLMs), we develop SFgen, an agentic
recognition and generation flow of symbol and footprint for electronic
components. SFgen achieves 86% accuracy for symbol generation and
80% accuracy for footprint generation. We use the SFgen method to
create SFnet, a database of symbols and footprints. It now has 1000
components and is expanding constantly, which lays the foundation for
automatic generation of PCB designs.
Keywords: MLLM · PCB design · Symbol · Footprint.
1 Introduction
Component libraries are crucial in printed circuit board (PCB) design, offering
designers a predefined set of electronic components for both PCB schematics
and layouts. These libraries provide a comprehensive set of resources, including
datasheets, schematic symbols, 2D footprints, and 3D models.
Traditionally, companies manually create symbols and footprints based on
datasheets to build component libraries. This manual process is labor-intensive
and error-prone. Additionally, the varied formats of datasheets from different
vendors complicate the implementation of a standardized design process. The
differing requirements of various electronic design automation (EDA) software
further add to the challenge, making it difficult to reuse library resources across
design platforms and thus increasing development costs. With the continuous
⋆ Equal contribution
⋆⋆ Corresponding authors

第 2 页
2
influx of new components into the market each year, a more efficient and auto-
matic method of constructing electronic component libraries is essential to keep
pace with technological advancements and market demands.
The heterogeneous formats of datasheets and the absence of large-scale datasets
have made it difficult for traditional artificial intelligence (AI) methods to cap-
ture component design details. However, multimodal large language models (MLLMs) [1–
3] along with prompt engineering [4–8] offer a promising solution to pick up es-
sential information in datasheets and generate accurate design files. Facilitated
by their extensive knowledge, MLLMs can tackle the challenge without retrain-
ing. On the other hand, as electronic designs become more and more compli-
cated, AI-copilot PCB design points out an opportunity to significantly reduce
design cycle while ensuring high design quality. The automatic component li-
brary construction serves as the necessary foundation for MLLMs to understand
and create PCB designs.
This paper presents an automatic electronic component library construction
pipeline, SFgen. As summarized in Fig. 1, SFgen utilizes MLLM to agentically
parse datasheets, and recognize and generate symbols and footprints for elec-
tronic components. Based on SFgen, we create a dataset, SFnet, that has more
than 1000 electronic components.
To assess the performance of generated designs, we introduce both quali-
tative and quantitative evaluation metrics. The qualitative evaluation focuses
on the aesthetic appeal, and the quantitative metrics measure the accuracy of
pin/shape counts and deviations in geometric dimensions. In addition, we con-
struct a benchmark dataset and evaluation protocol, consisting of 100 symbols
and footprints, each accompanied by its corresponding datasheet, to facilitate
rigorous testing and comparison.
MLLM
Datasheet
Template Library
Datasheet
 Symbol / Footprint
Manually 
designed
(a)Traditional
(b)SFgen
Time-consuming
Error-prone
Efficiently
Symbol /Footprint
Manual 
correction
（if wrong）
In-Context Learning
Chain-of-Thought
Visual Prompts
  Prompt
Footprint Diagram
Symbol Diagram
Pin Function 
  Recognization
   Generation
Fig. 1: Traditional manual design v.s. SFgen

第 3 页
3
To the best of our knowledge, SFgen is the first published study of MLLM-
driven agentic recognition and generation of PCB component designs. The pro-
posed method and the resulting SFnet dataset lay a solid foundation for the
automatic generation of PCB designs in the future. Our main contributions are
summarized as follows.
1. We propose SFgen, an MLLM-based agentic solution for symbol and foot-
print generation of PCB components.
2. We provide a benchmark testset consisting of datasheets and their corre-
sponding symbol and footprint files along with the evaluation protocol. The
benchmark facilitates rigorous testing and comparison of different methods.
3. Based on SFgen, we construct SFnet, a database encompassing more than
1,000 symbols and footprints of electronic components. As we know, this is
the first large-scale dataset for automatic electronic component generation.
2 SFgen Algorithms
This section provides the details of each step of SFgen.
2.1 Problem Definition
We define the automatic symbol and footprint generation as a conditional text
generation task, as most EDA software stores these content in text formats.
Inputs to the pipeline are datasheets containing pin configurations, pin function
descriptions, and footprint details, etc. The output symbols and footprints should
follow specific EDA software formats.
A component symbol refers to the graphical symbol used in schematic di-
agrams. It encompasses critical information for maintaining the precision and
integrity of the circuit design, including (1) pin function: the specific role of each
pin within a circuit, and (2) pin configuration: the layout and physical arrange-
ment of pins on a component or chip. A complete symbol should include correct
name, location, and type for each pin.
The footprint file is foundational for creating the layout, ensuring the cor-
rect installation of an electronic component. The essential information includes
(1) pad sizes, (2) pad placements, and (3) component body outline (the actual
space occupied by the component, which helps avoid physical conflicts between
components in layout). A complete footprint file should include the perimeter
coordinates for each pad polygon.
2.2 Algorithm Overview
Considering the conditional text generation task, we denote the dataset D =
{(xj, yj)}M
j=1, where ( xj, yj) is the j−th sample of the dataset, an (input con-
straint, output text) pair, while M is the total number of samples.
SFgen starts with information extraction from the datasheets, illustrated in
Fig. 2. Based on the open-source PDF parsing tool [9], the flow automatically

第 4 页
4
extracts various types of images from the datasheets and classifies them using an
image classifier to obtain key constraints required for component construction.
The images include symbol diagrams, footprint diagrams, pin-function tables,
etc. Critical information from the datasheets is summarized, such as component
manufacturer, device type, package format and pin count. Such information is
used to retrieve the best-match template from the Template Library for in-
context learning (ICL).
Images
(Diagrams&tables)
Symbol
Footprint
Pin function
Type
Productor
Pin-Num
Datasheet
 Image Classifier
CNN MLP
Images
(Diagrams & Tables) Extraction Result
Footprint Diagram
Symbol Diagram
Pin Function 
  Extraction
Symbol Diagram Footprint Diagram
Pin Function 
PDF Parser 
Tools
Fig. 2: The flow of information extraction from datasheets
As summarized in Fig. 1(b), k samples {(xj, yj)}k
j=1 are provided to SFgen
as ICL templates, where xj and yj are constraint and target file respectively. A
test directive is based on the constraint xtest, with the goal of generating high-
quality component library files ytest. The preamble R is the specific task, such
as “symbol generation” or “footprint generation”. The final prompt and outputs
can be formulated as follows.
P = [R; x1; y1; . . .; xk; yk; xtest]; y = M LLM(P ) (1)
2.3 Symbol Generation
Fig. 3 illustrates the symbol generation process employed by SFgen. Our expecta-
tion from SFgen is to automate the generation of the corresponding symbol based
on the input datasheet, with the prompt serving as the key to this automation.
We have designed the prompt to integrate input constraints, ICL examples, task
descriptions, and other relevant information. The MLLM then processes inputs
and provides the necessary logical and spatial location parameters to generate
constraint-compliant symbol files. SFgen starts by compiling the few-shot ICL
examples that encompass pin functional descriptions, configurations, and corre-
sponding symbol files. The examples exemplify the detailed mapping between
input and output and guide the MLLM to follow the specified output format.The improved accuracy ensures the correct number of pins and pin naming.
Furthermore, SFgen learns to create legible symbol files by considering aspects
such as polygon dimensions, the interconnections between lines and polygons,
spacing between lines, and text formatting. This multifaceted learning approach
equips SFgen to accommodate various file formats. These files can be visualized

第 5 页
5
Datasheet 
under Study
MLLM
Template Library
Pin Function 
Descriptions Pin Configuration
 Symbol 
Best-match Template for ICL
Output
Datasheet under Study:
Pin Configuration,
Pin Function Descriptions
Template for ICL：
Pin Constraints,
 Symbol
Preamble:
Task Description，
 Symbol Generation
Prompt
Visualize
EDA Software
(1)
(2) (3)
(4)
Fig. 3: Symbol generation flow: (1) select best-matching ICL cases from tem-
plate library, (2) construct prompt with multimodal information from target
datasheet, (3) generate symbol file with MLLM, (4) visualize and compare
against ground truth (GT)
on dedicated EDA software, which also allows for further manual modifications,
thereby reducing the manual effort required in the symbol generation process.
2.4 F ootprint Generation
The flow of footprint generation is summarized in Fig. 4. First, footprint infor-
mation is extracted from the input datasheet, including the size and position of
each pad. Similar to symbol generation, SFgen uses few-shot examples in ICL,
which help the MLLM understand the constraints of pad locations and sizes.
SFgen is capable of generating different file formats depending on the template
format.
MLLM
CoT:
Description,
Generation
Template for ICL：
Footprint Detail,
Footprint
Preamble:
Task Description，
Footprint Generation
Footprint
Best-match Template for ICL
Symmetry,PositionMark Pad Number
Visual Prompt Generator Prompt
Modified Prompt
Footprint Detail
Visual Prompt:
Pad Number
 Template 
Library
Datasheet 
under Study
1
4 5
32
6
Output
Visualize
EDA Software
(1)
(2)
(3) (4)
(5)
(6)
Fig. 4: Footprint generation flow: (1) attach visual prompt to datasheet im-
ages,(2) select best-matching ICL cases from template library, (3) construct full
prompt, (4) generate footprint with MLLM, (5) incrementally improve footprint
through prompt modification, (6) compare against GT
Unlike symbol generation, we introduce visual prompt (VP) for footprint
generation to enhance SFgen’s ability to understand the pad dimensions and
positions. Fig. 5 illustrates how the VP generator annotates each pad with a
numerical identifier. The identifiers help the MLLM to accurately recognize the
number of pads, pad locations, and dimensions. In addition to annotations in
images, we introduce CoT with visual information in the text-based prompt.
The prompt requests the model to describe the pads based on given indexes,
which guides the model in processing input information more logically.
Prompts for footprint generation integrate the constraints, templates, and
add-on visual information. SFgen responds to the input by generating a prelimi-

第 6 页
6
Question
Without VP
With VP
Question:This figure shows a footprint of an electronic 
component. Describe the number of pads in this footprint 
and explain what 3, 5.08, and 11 represent between the 
pads.
1
4
5
3
2
6
Without VP: A pad map (footprint) consisting of four 
pads can be seen. “3” - Pad Dimensions，“5.08” -
vertical distance，"11" -horizontal length
W ith V P :  S ix  p a d s  a r e  s h o w n .  " 3 "  -  P a d 
Dimensions,"5.08"-vertical distance between the 
Pad 1 to 3 and Pad 4 to 6,  "11"-horizontal length 
from  pad 1 to pad 3
Base Footprint 
Detail Mark pad Number
Fig. 5: Illustration of visual prompt (VP): without VP, the LLM incorrectly
answers four pads; with VP, the LLM correctly answers six pads.
nary footprint file that can be used by EDA software for visualization. However,
the preliminary outputs may contain errors, particularly in the symmetry and po-
sitions of pads. Hence, we introduce the modified prompt, which checks footprint
and corrects errors step by step. Specifically, the visual images are re-imported
into SFgen, and footprints are further optimized to ensure that the final outputs
meet the design requirements.
3 Evaluation Protocol
3.1 Benchmark Construction
Due to the extensive variety of electronic components, there are significant dif-
ferences in their functionalities and package configurations. These differences di-
rectly impact the complexity of generating component symbols and footprints.
To systematically evaluate the reliability and compatibility of SFgen, we selected
a representative evaluation dataset. The dataset ensured diversity by selecting
components based on the number of pins, device types, and the availability of
both symbol and footprint data. Table 1 summarizes the dataset and Fig. 6
presents the data distribution.
3.2 Evaluation Metrics
For evaluate the generated results, the primary focus is on the accurate counts
and types of the generated pins and pads. Any discrepancies in these quanti-
ties are considered prediction errors. The definitions of ACC N and ACC T are

第 7 页
7
Table 1: Evaluation Dataset
Symbol and F ootprint Generation
Group Type Complexity Level Pin-Number Components Type Quantity
Basic Simple 1-5 R, L, C, D, Fuse, LED, Switch 25
Standard Moderate 6-20 IC, Sensor, Transistor 50
Complex Difficult 21-40 IC, Module 15
High-Density Extremely Difficult 41-100 IC 10
0
5
10
15
20
25
30
35
40
0
10
20
30
40
50
60
1-5 6-20 21-40 41-100
Average Size(KB)
Number of data
Number of Pins/Pads
Symbol of Files Footprint of Files Symbol Average Size(KB) Footprint Average Size(KB)
Fig. 6: Evaluation dataset statistics
provided in Equations (2) and (3). ACC N quantifies the accuracy of pin/pad
counts, defined as the ratio of components with the correct pin/pad number to
the total number of components. ACC T evaluates the type accuracy by compar-
ing the number of correctly typed pins/pads to the total number of pins/pads. It
is important to note that ACC T is computed only when the pin or pad count is
accurate. If there is a discrepancy in the pin or pad count, the entire component
is deemed incorrect.
ACC N = Number Components with Correct Pins/Pads
Total Components (2)
ACC T = Number Correct Typed Pins/Pads
Total Pins/Pads (3)
Size and position accuracy are crucial aspects of footprint evaluation, and
we assess these characteristics when the types and numbers of pads are cor-
rect. Specifically, we calculate the sum of normalized area differences to measure
the overall difference between the generated pad size and the actual pad size.
Similarly, we compute the absolute sum of the normalized coordinate positional
differences for each pad to evaluate position accuracy. The definitions of DifA
and DifP are provided in Equations (4) and (5).

第 8 页
8
DifA =
NX
i=1
|Areagen,i − AreaGT,i|
AreaGT,i
(4)
DifP =
NX
i=1
|Posgen,i − PosGT,i|p
AreaGT,i
(5)
In the equations, Area denotes the area of the pad,Pos denotes the position of
the pad, i denotes the i-th component, and the subscripts gen and GT represent
the generation of SFgen versus ground truth, respectively.
Other than quantitative evaluations, we design mean opinion score for sym-
bol (MOS-S) and mean opinion score for footprint (MOS-F) based on designer
expertise to thoroughly assess the design quality. Assessments are conducted
from four dimensions: accuracy, readability, usability, and aesthetics. Evaluators
rate the overall quality of the generated symbols and footprints on a scale rang-
ing from 1 to 5, with higher scores denoting superior quality. As a subjective
evaluation method, the scores evaluate how the generated design style conforms
to the existing ones in practical applications. Table 2 outlines the specific scoring
criteria.
Table 2: MOS Evaluation Criteria
Quality Level MOS Evaluation Criteria
Excellent 5 Excellent quality; no adjustments.
Good 4 Good quality; only minor adjustments.
Average 3 Average quality; some adjustments.
Poor 2 Poor quality; numerous adjustments.
Inferior 1 Inferior quality; significant adjustments.
4 Experiments
4.1 Experiment Setting
We implemented the SFgen framework and conducted experiments using the
state-of-the-art MLLM, GPT4. All the experiments were performed through
API calls. Visualization is done through KiCad 8.0.5. Full prompts are shown in
Fig. 10, Fig. 11, and Fig. 12 in the Appendix.
4.2 Symbol Generation Results
As previously discussed, the two metrics, ACC N and ACC T , are used to mea-
sure the quality of the generated symbols. Table 3 presents the results of SFgen

第 9 页
9
Table 3: Evaluation of Generated Symbols
Group ACC N (↑ ) ACC T (↑ ) MOS
Basic 96.00% 96.36% 5
Standard 86.00% 83.46% 4
Complex 73.33% 84.80% 3
High-Density 0.00% 49.32% 1
across four test sets. In the Basic Group, 96% of the test outcomes were ideal.
However, as the complexity increases, the performance deteriorates. The exper-
imental results indicate that in three out of four test sets, SFgen can generate
a large number of usable Symbol files. Even in the most complex scenarios, al-
though it cannot directly produce standard symbols, it achieves an accuracy of
49.32% in generating pins.
Output Ground Truth Output Ground Truth Output Ground Truth
Symbol generation of L293DDSymbol generation of L, D, SW Symbol generation of NRF905
Fig. 7: Visualization results of generated symbols
Fig. 7 shows the comparison between the generated symbols and ground
truth (GT) for sample components. The visualizations verify that the symbols
generated by SFgen are visually consistent with GT. Meanwhile, they are highly
accurate in terms of functional layout. Furthermore, SFgen successfully addresses
some finer requirements such as the correct pin labels and positions, and ensures
the symbols are easy to read. The high degree of consistency and accuracy ex-
emplify the reliability and validity of SFgen in real-world applications, making
it a promising tool to replace labor-intensive design processes.
4.3 F ootprint Generation Results
Four metrics, ACC N , ACC T , DifA, and DifP , are used to measure the quality
of the generated footprints, Table 4 summarizes the results. Similar to evalua-
tion of symbol generation, SFgen achieves satisfactory results in both the Basic
Group and Standard Group, with ACC N reaching 96% and 80% respectively.
Additionally, DifA remains below 10% in both groups. As the complexity of the

第 10 页
10
Footprint generation of NE555P Footprint generation of ATTINY2313-20SUFootprint generation of 24AA16-I_SN
Output Ground Truth Output Ground TruthOutput Ground Truth
Fig. 8: Visualization results of generated footprints
footprint increases, its performance deteriorates, with a sharp decline in accu-
racy observed in the High-Density Group. This is due to the current limitations
of the MLLM in accurately recognizing complex images.
Table 4: Evaluation of Generated Footprints
Group ACC N (↑ ) ACC T (↑ ) Dif A (↓ ) Dif P (↓ ) MOS
Basic 96.00% 94.54% 4.26% 8.23% 5
Standard 80.00% 89.8% 8.76% 15.3% 4
Complex 46.67% 65.59% 11.18% 28.87% 2
High-Density 0.00% 35.4% 19.32% 42.5% 1
Fig. 8 shows some examples of footprint visualization results. The generated
footprints consistently reflect the pad shapes, sizes, and spacing, demonstrat-
ing the ability of SFgen to ensure design accuracy. As the generated files are
text-based and editable, the generated footprints can adhere to the required
metallization patterns with minor modifications through EDA platforms.
4.4 Ablation Study for F ootprint Generation
We conduct a limited number of experiments on the footprint generation task,
utilizing VP and Modified prompt to further enhance the quality of footprint
generation. As shown in Fig. 9, for complex circuit components, the use of chain
of thought (CoT) technology initially produced suboptimal results. By adding
an additional mark to each pad as a VP and combining this with COT for
regeneration, the positioning accuracy of each pad was enhanced. Further modi-
fications to these results yielded a generation quality that was considerably more
satisfactory.
5 SFnet Database
Based on SFgen, we develop SFnet, which includes 1000 electronic datasheets
and generate corresponding symbols and footprints. SFnet encompasses a variety

第 11 页
11
Ground TruthBaseline ModifiedVP+COTVPCOT
(b)Footprint generation of  TB6612FNG
(a)Footprint generation of  CP2102-GMR
Fig. 9: Ablation study of footprint generation
of electronic components, which are listed in the Table 5, with integrated circuits
(ICs) constituting the majority. As we know, this is the first large-scale dataset
for electronic components.
Table 5: Categories and Quantities of SFnet Dataset
Component Type Quantity Component Type Quantity
IC 722 Resistor 165
Capacitor 37 Sensor 19
Transistor 15 Diode 11
Inductor 6 LED 6
Fuse 5 Module 4
MOS 3 Crystal Oscillator 3
Display 1 ESD 1
Antenna 1 Relay 1
6 Conclusions and Future Work
This paper presents an MLLM-driven pipeline, SFgen, which agentically ‌ recog-
nizes and generates symbol and footprint files for electronic components. To en-
hance MLLM’s understanding of design details and generate accurate design, we
performed various prompt strategies including in-context learning (ICL), visual
prompting (VP), and chain of thought (CoT). Compared to the labor-intensive
manual design process, SFgen automatically generates highly correct symbols
and footprints within 3-5 minutes per component. Based on SFgen, we con-
struct SFnet, a database includes 1000 electronic components datasheet, symbol
and foorprint.

第 12 页
12
Our future work includes extending SFgen to a much wider set of electronic
components. Meanwhile, we plan to open-source SFnet to further promote re-
search and development in this field. As a starting point, we believe that SFgen
has laid a solid foundation for MLLM’s understanding of PCB schematics. In
the future, it is possible to facilitate explorations of MLLM’s application in au-
tomatic PCB designs.
References
1. J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, F. L. Aleman, D. Almeida,
J. Altenschmidt, S. Altman, S. Anadkat, et al., “Gpt-4 technical report,” arXiv
preprint arXiv:2303.08774, 2023.
2. G. Team, R. Anil, S. Borgeaud, Y. Wu, J.-B. Alayrac, J. Yu, R. Soricut, J. Schalk-
wyk, A. M. Dai, A. Hauth, et al., “Gemini: a family of highly capable multimodal
models,” arXiv preprint arXiv:2312.11805, 2023.
3. H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux, T. Lacroix,
B. Rozi` ere, N. Goyal, E. Hambro, F. Azhar, et al., “Llama: Open and efficient
foundation language models,” arXiv preprint arXiv:2302.13971, 2023.
4. J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le, D. Zhou,
et al., “Chain-of-thought prompting elicits reasoning in large language models,”
Advances in Neural Information Processing Systems, vol. 35, pp. 24824–24837, 2022.
5. Y. Wu, P. Zhang, W. Xiong, B. Oguz, J. C. Gee, and Y. Nie, “The role of chain-of-
thought in complex vision-language reasoning task,” arXiv e-prints, pp. arXiv–2311,
2023.
6. J. Yang, H. Zhang, F. Li, X. Zou, C. Li, and J. Gao, “Set-of-mark prompting un-
leashes extraordinary visual grounding in gpt-4v,” arXiv preprint arXiv:2310.11441,
2023.
7. J. Lin, J. Guo, S. Sun, Z. Yang, J.-G. Lou, and D. Zhang, “Layoutprompter: Awaken
the design ability of large language models,” Advances in Neural Information Pro-
cessing Systems, vol. 36, 2024.
8. P. Wang, S. Bai, S. Tan, S. Wang, Z. Fan, J. Bai, K. Chen, X. Liu, J. Wang, W. Ge,
et al., “Qwen2-vl: Enhancing vision-language model’s perception of the world at any
resolution,” arXiv preprint arXiv:2409.12191, 2024.
9. B. Wang, C. Xu, X. Zhao, L. Ouyang, F. Wu, Z. Zhao, R. Xu, K. Liu, Y. Qu,
F. Shang, B. Zhang, L. Wei, Z. Sui, W. Li, B. Shi, Y. Qiao, D. Lin, and C. He,
“Mineru: An open-source solution for precise document content extraction,” 2024.

第 13 页
13
7 Appendix : Prompt Details
Fig. 10: Design prompts for symbol generation

第 14 页
14
Fig. 11: Modified prompts for footprint generation
Fig. 12: Design prompts for footprint generation
