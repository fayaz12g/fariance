import React, { useState, useEffect } from 'react';
import './App.css';
import modItemsCatalog from './mod_items_catalog.json';

const WOOD_TYPES = ["oak", "spruce", "birch", "jungle", "acacia", "dark_oak", "mangrove", "cherry", "crimson", "warped", "bamboo"];
const TOOL_TYPES = ["sword", "pickaxe", "shovel", "hoe", "axe"];
const COPPER_TYPES = ["shiny_copper", "weathered_copper", "exposed_copper", "oxidized_copper"]
const MATERIAL_TYPES = [...WOOD_TYPES, ...COPPER_TYPES, "iron", "diamond", "copper", "gold", "netherite", "amethyst", "diorite", "andesite", "granite", "blackstone", "cobblestone", "redstone", "lapis", "quartz", "deepslate"];
const STICK_TYPES = [...WOOD_TYPES, "blaze", "breeze"];


const ToolCard = ({ name, imageSrc }) => (
  <div className="tool-card">
    <img src={imageSrc} alt={name} onError={(e) => { console.error(`Failed to load image: ${imageSrc}`); e.target.src = 'placeholder.png'; }} />
    <h3>{name}</h3>
  </div>
);

const FilterButton = ({ name, onClick, isActive }) => (
  <button
    onClick={onClick}
    className={`filter-button ${isActive ? 'active' : ''}`}
  >
    <p>{name}</p>
  </button>
);

const App = () => {
  const [modData, setModData] = useState({ tools: [] });
  const [filters, setFilters] = useState({ stick: null, material: null, toolType: null });
  const [searchTerm, setSearchTerm] = useState('');
  const [activeTab, setActiveTab] = useState('all');
  const [error, setError] = useState(null);

  useEffect(() => {
    try {
      console.log('Loading mod data...');
      setModData(modItemsCatalog);
      console.log('Mod data loaded:', modItemsCatalog);
    } catch (error) {
      console.error("Error loading mod data:", error);
      setError(`Failed to load mod data: ${error.message}. Please check the console for more details.`);
    }
  }, []);

  useEffect(() => {
    console.log('Current modData:', modData);
  }, [modData]);

  const filteredTools = modData.tools.filter(tool => {
    const matchesStick = !filters.stick || tool.stick === filters.stick;
    const matchesMaterial = !filters.material || tool.material === filters.material;
    const matchesToolType = !filters.toolType || tool.type === filters.toolType;
    const matchesSearch = tool.name.toLowerCase().includes(searchTerm.toLowerCase());
    return matchesStick && matchesMaterial && matchesToolType && matchesSearch;
  });

  console.log('Filtered tools:', filteredTools);

  if (error) {
    return (
      <div className="error-container">
        <h1>Error</h1>
        <p>{error}</p>
        <p>Please ensure that the mod_items_catalog.json file is present in the src folder and contains valid JSON data.</p>
      </div>
    );
  }

  const handleResetFilter = (filterType) => {
    setFilters({ ...filters, [filterType]: null });
  };

  return (
    <div className="container">
      <h1>WoodStuff Mod Showcase</h1>
      <p>Discover over {modData.tools.length} new tools added to Minecraft!</p>

      <div className="tabs">
        <button onClick={() => setActiveTab('all')} className={activeTab === 'all' ? 'active' : ''}>All Tools</button>
        <button onClick={() => setActiveTab('sticks')} className={activeTab === 'sticks' ? 'active' : ''}>Sticks</button>
        <button onClick={() => setActiveTab('materials')} className={activeTab === 'materials' ? 'active' : ''}>Materials</button>
        <button onClick={() => setActiveTab('tools')} className={activeTab === 'tools' ? 'active' : ''}>Tool Types</button>
      </div>

      <div className="tab-content">
        {activeTab === 'all' && (
          <>
            <input
              type="text"
              placeholder="Search tools..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="search-input"
            />
            <div className="tool-grid">
              {filteredTools.map((tool, index) => (
                <ToolCard
                  key={index}
                  name={tool.name}
                  imageSrc={tool.imagePath}
                />
              ))}
            </div>
          </>
        )}

        {activeTab === 'sticks' && (
          <>
            <div className="filter-buttons">
              <FilterButton
                name="All"
                onClick={() => handleResetFilter('stick')}
                isActive={filters.stick === null}
              />
              {STICK_TYPES.map((stick) => (
                <FilterButton
                  key={stick}
                  name={stick}
                  onClick={() => setFilters({ ...filters, stick: stick })}
                  isActive={filters.stick === stick}
                />
              ))}
            </div>
            <div className="tool-grid">
              {filteredTools.map((tool, index) => (
                <ToolCard
                  key={index}
                  imageSrc={tool.imagePath}
                  name={tool.name}
                />
              ))}
            </div>
          </>
        )}

        {activeTab === 'materials' && (
          <>
            <div className="filter-buttons">
              <FilterButton
                name="All"
                onClick={() => handleResetFilter('material')}
                isActive={filters.material === null}
              />
              {MATERIAL_TYPES.map((material) => (
                <FilterButton
                  key={material}
                  name={material}
                  onClick={() => setFilters({ ...filters, material: material })}
                  isActive={filters.material === material}
                />
              ))}
            </div>
            <div className="tool-grid">
              {filteredTools.map((tool, index) => (
                <ToolCard
                  key={index}
                  imageSrc={tool.imagePath}
                  name={tool.name}
                />
              ))}
            </div>
          </>
        )}

        {activeTab === 'tools' && (
          <>
            <div className="filter-buttons">
              <FilterButton
                name="All"
                onClick={() => handleResetFilter('toolType')}
                isActive={filters.toolType === null}
              />
              {TOOL_TYPES.map((toolType) => (
                <FilterButton
                  key={toolType}
                  name={toolType}
                  onClick={() => setFilters({ ...filters, toolType: toolType })}
                  isActive={filters.toolType === toolType}
                />
              ))}
            </div>
            <div className="tool-grid">
              {filteredTools.map((tool, index) => (
                <ToolCard
                  key={index}
                  imageSrc={tool.imagePath}
                  name={tool.name}
                />
              ))}
            </div>
          </>
        )}
      </div>
    </div>
  );
};

export default App;
