import { type QualityGateRule } from "@allurereport/plugin-api";

export const passRateCriticalsRule: QualityGateRule<number> = {
  rule: "passRateCriticals",
  message: ({ actual, expected }) =>
    `The pass rate of tests with critical severity label ${String(actual)} is less than ${String(expected)}`,
  validate: async ({ trs, expected, state1 = 0, state2 = 0 }) => {
    // find all tests with the critical severity label
    const withSeverities = trs.filter((tr) => tr.labels.some((label) => label.name === "severity" && label.value === "critical"));
    const withSeveritiesPass = withSeverities.filter((tr) => tr.status === "passed");
    
    // add previous "actual" value to the new one; state always equals to the previously returned actual property
    const actualWithSeverities = withSeverities.length + state1;
    const actualWithSeveritiesPass = withSeveritiesPass.length + state2;

    return {
      // the field tells us the rule's status
      success: actualWithSeveritiesPass / actualWithSeverities >= expected,
      // actual result
      actualWithSeverities,
      actualWithSeveritiesPass,
      // expected result given from the runtime configuration
      expected,
    };
  },
};