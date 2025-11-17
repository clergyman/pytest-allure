export default {
  name: "Allure Report 3",
  output: "./allure-report",
  qualityGate: {
    rules: [
      {
        maxFailures: 3,
        fastFail: true
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