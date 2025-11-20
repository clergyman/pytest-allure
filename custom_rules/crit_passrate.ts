import { type QualityGateRule } from "allure/rules";

export const passRateCriticalsRule: QualityGateRule<number, [number, number]> = {
  rule: "passRateCriticals",
  message: ({ actual, expected }) =>
    `The pass rate of tests with critical severity label ${(actual)} is less than ${expected}`,
  validate: async ({ trs, expected, state }) => {
    console.log("STATE: ", state);
    
    // find all tests with the critical severity label 
    const withSeverities = trs.filter((tr) => tr.labels.some((label) => label.name === "severity" && ["critical","blocker"].includes(label.value) ));
    // find how many of them passed
    const withSeveritiesPass = withSeverities.filter((tr) => tr.status === "passed");
    console.log("WITH SEVERITIES: ", withSeverities.length);
    console.log("WITH SEVERITIES PASS: ", withSeveritiesPass.length);
    

    const previous = state.getResult() ?? [0,0];


    const actualWithSeverities = withSeverities.length + previous[0];
    const actualWithSeveritiesPass = withSeveritiesPass.length + previous[1];


    // count actual pass rate based on previous state
    const actual = actualWithSeveritiesPass/actualWithSeverities;
    
    state.setResult([actualWithSeverities, actualWithSeveritiesPass]);
    const passed = actual >= expected;

    
    return {
      // the field tells us the rule's status
      success: passed,
      // actual result
      actual: actual,
    };
  },
};