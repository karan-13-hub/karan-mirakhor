import matter from 'gray-matter';
import { remark } from 'remark';
import html from 'remark-html';

// Import generated content data
import { 
  getAllContent as getAllContentFromData,
  getContentBySlug as getContentBySlugFromData,
  getSectionContent as getSectionContentFromData
} from './content-data';

// Re-export functions
export const getAllContent = getAllContentFromData;
export const getContentBySlug = getContentBySlugFromData;
export const getSectionContent = getSectionContentFromData;

export async function markdownToHtml(markdown) {
  const result = await remark().use(html).process(markdown);
  return result.toString();
}
