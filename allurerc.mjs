import { passRateCriticalsRule } from "./custom_rules/crit_passrate.ts"
import { passRateNonCriticalsRule } from "./custom_rules/non_crit_passrate.ts"
import { maxFailuresRule } from "@allurereport/core"
import { successRateRule } from "allure/rules"

export default {
  name: "Allure Report 3",
  output: "./allure-report",
  qualityGate: {
    rules: [
      {
        
        passRateCriticals: 0.95,
        maxFailures: 1
      },
      {
        successRate: 0.90,
        filter: (tr) => tr.labels.some((label) => label.name === "severity" && !["critical","blocker"].includes(label.value) )
      }
    ],
    use: [
      {...successRateRule
        message: ({ actual, expected }) => `We are not doing good: ${actual} >= ${expected}`
      }, 
      {passRateCriticalsRule}, 
      {maxFailuresRule}
      ]
  },
  plugins: {
    awesome: {
      options: {
        singleFile: true,
        reportLanguage: "en",
        reportName: "Allure 3 Report",
        groupBy: ["module", "parentSuite", "suite", "subSuite"],
      },
    }
  },
  variables: {}, //environment.properties check who wins
  environments: {
    chromium: {
      matcher: ({ labels }) => labels.find(({ name, value }) => name === "driver" && value === "chromium"),
    },
    firefox: {
      matcher: ({ labels }) => labels.find(({ name, value }) => name === "driver" && value === "firefox"),
    },
    safari: {
      matcher: ({ labels }) => labels.find(({ name, value }) => name === "driver" && value === "webkit"),
    },
    macos: {
      matcher: ({ labels }) => labels.find(({ name, value }) => name === "os" && value === "macos"),
    },
    windows: {
      matcher: ({ labels }) => labels.find(({ name, value }) => name === "os" && value === "windows"),
    },
    linux: {
      matcher: ({ labels }) => labels.find(({ name, value }) => name === "os" && value === "linux"),
    }
  },
};