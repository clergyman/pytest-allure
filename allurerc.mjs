import { passRateCriticalsRule } from "./custom_rules/crit_passrate.js";
import { successRateRule } from "allure/rules";
import { defineConfig } from "allure";


// const { MY_ENV } = process.env.MY_ENV;
// console.log("AAAAAAA MY_ENV: ", MY_ENV);

//console.log("BAAAAAAAAA process envs", process.env);

let { MY_ENV, MY_ENV2 } = process.env;


export default defineConfig({
  name: "Allure Report 3",
  output: "./allure-report",
  qualityGate: {
    rules: [
      {
        maxFailures: 0,
        passRateCriticals: MY_ENV2 ? Number(MY_ENV2) : 0.95,
      },
      {
        successRate: MY_ENV ? Number(MY_ENV) : 0.90,
        filter: (tr) =>
          tr.labels.some( 
            (label) =>
              label.name === "severity" &&
              !["critical", "blocker"].includes(label.value),
          ),
      },
    ],
    use: [
      passRateCriticalsRule,
      {
        ...successRateRule,
        message: ({ actual, expected }) =>
          `We are not doing good: ${actual} >= ${expected}`,
      },
    ],
  },
  plugins: {
    awesome: {
      options: {
        singleFile: true,
        reportLanguage: "en",
        reportName: "Allure 3 Report",
        groupBy: ["module", "parentSuite", "suite", "subSuite"],
      },
    },
  },
  variables: {}, //environment.properties check who wins
  environments: {
    chromium: {
      matcher: ({ labels }) =>
        labels.find(
          ({ name, value }) => name === "driver" && value === "chromium",
        ),
    },
    firefox: {
      matcher: ({ labels }) =>
        labels.find(
          ({ name, value }) => name === "driver" && value === "firefox",
        ),
    },
    safari: {
      matcher: ({ labels }) =>
        labels.find(
          ({ name, value }) => name === "driver" && value === "webkit",
        ),
    },
    macos: {
      matcher: ({ labels }) =>
        labels.find(({ name, value }) => name === "os" && value === "macos"),
    },
    windows: {
      matcher: ({ labels }) =>
        labels.find(({ name, value }) => name === "os" && value === "windows"),
    },
    linux: {
      matcher: ({ labels }) =>
        labels.find(({ name, value }) => name === "os" && value === "linux"),
    },
  },
});
