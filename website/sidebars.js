/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide a category with custom icons and labels
 */

// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  // By default, Docusaurus generates a sidebar from the docs folder structure
  tutorialSidebar: [
    {
      type: 'doc',
      id: 'matrices',
      label: '📊 Data Download Vault',
    },
    {
      type: 'doc',
      id: 'cry_for_israel_unabridged',
      label: '📜 Unabridged Manuscript',
    },
  ],
};

module.exports = sidebars;
