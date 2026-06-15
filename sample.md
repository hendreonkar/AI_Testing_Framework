flowchart TD
    %% Outer Loop Driver (Design Exploration)
    DE[Optimization / DOE Adapter] -->|Design Variables| SEQ[Execution Sequence]

    %% Execution Sequence (nested)
    subgraph SEQ [Execution Controls – Nested Sequence]
        direction TB
        ST[Structural Simulation (Abaqus) Adapter] -->|Structural Results| CALC[Calculator Adapter]
        FL[Fluid Simulation (CFD) Adapter] -->|Fluid Results| CALC
        CALC -->|Intermediate Scalars| PY[Python Adapter]
        PY -->|Parsed Text| TXT[Text Parser Adapter]
        TXT -->|Constraints & Flags| DE
    end

    %% Data Exchange & Artifact Generation
    DE -->|Export Trigger| EX3D[Export 3DXML Adapter]
    DE -->|Export Trigger| EXAB[Export Abaqus .inp Adapter]

    %% Automated Reporting
    EX3D -->|3D Model| REP[HTML Report Generator Adapter]
    EXAB -->|Abaqus Input| REP
    CALC -->|Performance Metrics| REP
    PY -->|Custom Metrics| REP
    TXT -->|Constraint Flags| REP

    %% Loop back for next iteration
    REP -->|Iteration Complete| DE
