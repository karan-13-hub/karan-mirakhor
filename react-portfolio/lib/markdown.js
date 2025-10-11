import matter from 'gray-matter';
import { remark } from 'remark';
import html from 'remark-html';
import fs from 'fs';
import path from 'path';

// Content directory path
const contentDirectory = path.join(process.cwd(), 'content');

// Load markdown files from content directory
function loadMarkdownFiles(directory) {
  try {
    const fullPath = path.join(contentDirectory, directory);
    if (!fs.existsSync(fullPath)) {
      return [];
    }
    
    const fileNames = fs.readdirSync(fullPath);
    const markdownFiles = fileNames.filter(name => name.endsWith('.md'));
    
    return markdownFiles.map(fileName => {
      const fullFilePath = path.join(fullPath, fileName);
      const fileContents = fs.readFileSync(fullFilePath, 'utf8');
      const { data, content } = matter(fileContents);
      
      return {
        ...data,
        content: content.trim(),
        slug: fileName.replace(/\.md$/, '')
      };
    });
  } catch (error) {
    console.error(`Error loading markdown files from ${directory}:`, error);
    return [];
  }
}

// Load single markdown file
function loadMarkdownFile(fileName) {
  try {
    const fullPath = path.join(contentDirectory, `${fileName}.md`);
    if (!fs.existsSync(fullPath)) {
      return null;
    }
    
    const fileContents = fs.readFileSync(fullPath, 'utf8');
    const { data, content } = matter(fileContents);
    
    return {
      ...data,
      content: content.trim()
    };
  } catch (error) {
    console.error(`Error loading markdown file ${fileName}:`, error);
    return null;
  }
}

export function getAllContent(type) {
  return loadMarkdownFiles(type);
}

export function getContentBySlug(type, slug) {
  const allContent = getAllContent(type);
  return allContent.find(item => item.slug === slug) || null;
}

export function getSectionContent(sectionName) {
  return loadMarkdownFile(sectionName);
}

export async function markdownToHtml(markdown) {
  const result = await remark().use(html).process(markdown);
  return result.toString();
}
