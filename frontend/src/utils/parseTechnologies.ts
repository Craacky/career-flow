const parseTechnologies = (techString: string): string[] => {
  if (!techString) return [];
  
  // Split by common delimiters and clean up
  return techString
    .split(/[,;|]/)
    .map(tech => tech.trim())
    .filter(tech => tech.length > 0);
};

const formatTechnologies = (technologies: string[]): string => {
  return technologies.join(', ');
};

export { parseTechnologies, formatTechnologies };