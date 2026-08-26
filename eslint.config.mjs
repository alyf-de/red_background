import { createRequire } from "node:module";

// Resolve via CJS so pre-commit's NODE_PATH (additional_dependencies) is honored.
const require = createRequire(import.meta.url);
const globals = require("globals");
const js = require("@eslint/js");

export default [
	js.configs.recommended,
	{
		languageOptions: {
			ecmaVersion: "latest",
			sourceType: "module",
			globals: {
				...globals.browser,
				frappe: "readonly",
				__: "readonly",
			},
		},
		rules: {
			"no-console": "warn",
			"no-unused-vars": "warn",
		},
	},
];
