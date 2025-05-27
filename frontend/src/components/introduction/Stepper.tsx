import React, { useState } from "react";

interface StepperProps {
  steps: string[];
  components: React.ReactNode[];
}

const Stepper: React.FC<StepperProps> = ({ steps, components }) => {
  const [currentStep, setCurrentStep] = useState(0);

  const progressPercent = ((currentStep + 1) / steps.length) * 100;

  return (
    <div style={{ maxWidth: 400, margin: "20px auto" }}>
      <h3>{steps[currentStep]}</h3>
      <progress className="uk-progress" value={progressPercent} max="100"></progress>

      <div style={{ marginTop: 20 }}>
        {components[currentStep]}
      </div>

      <div style={{ marginTop: 20, display: "flex", justifyContent: "space-between" }}>
        <button
          className="uk-button uk-button-default"
          onClick={() => setCurrentStep((s) => Math.max(s - 1, 0))}
          disabled={currentStep === 0}
        >
          Back
        </button>

        <button
          className="uk-button uk-button-primary"
          onClick={() => setCurrentStep((s) => Math.min(s + 1, steps.length - 1))}
          disabled={currentStep === steps.length - 1}
        >
          Next
        </button>
      </div>
    </div>
  );
};

export default Stepper;