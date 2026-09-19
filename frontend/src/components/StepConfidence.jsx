export default function StepConfidence({
  step,
}) {

  return (

    <div>

      <strong>
        Step {step.step_number}
      </strong>

      <div>
        Verification:{" "}
        {step.verification_score.toFixed(2)}
      </div>

      <div>
        Consistency:{" "}
        {step.consistency_score.toFixed(2)}
      </div>

      <div>
        Confidence:{" "}
        {step.fused_confidence.toFixed(2)}
      </div>

    </div>
  );
}