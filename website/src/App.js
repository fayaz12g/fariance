import React, { useState, useEffect } from 'react';
import './App.css';
import modItemsCatalog from './mod_items_catalog.json';

const WOOD_TYPES = ["oak", "dark_oak", "pale_oak", "spruce", "birch", "jungle", "acacia", "mangrove", "cherry", "crimson", "warped", "bamboo", "tyrian", "charred"];
const TOOL_TYPES = ["sword", "pickaxe", "shovel", "hoe", "axe"];
const COPPER_TYPES = ["shiny_copper", "weathered_copper", "exposed_copper", "oxidized_copper"]
const MATERIAL_TYPES = [...WOOD_TYPES, ...COPPER_TYPES, "iron", "diamond", "copper", "gold", "netherite", "amethyst", "diorite", "andesite", "granite", "blackstone", "cobblestone", "redstone", "lapis", "quartz", "deepslate", "sandstone", "red_sandstone", "end_stone"];
const STICK_TYPES = [...WOOD_TYPES.map(s => "stripped_" + s), ...WOOD_TYPES, "blaze", "breeze"];

const ToolCard = ({ name, imageSrc, material }) => {
  return (
    <div className="tool-card">
        <img
          src={imageSrc}
          alt={name}
          onError={(e) => { console.error(`Failed to load image: ${imageSrc}`); e.target.src = 'placeholder.png'; }}
          style={{ width: '100%', height: 'auto', marginTop: '20px', imageRendering: 'pixelated' }}
        />
      <h3>{name}</h3>
    </div>
  );
};

const FilterButton = ({ name, onClick, isActive, imagePath }) => (
  <button
    onClick={onClick}
    className={`filter-button ${isActive ? 'active' : ''}`}
  >
    {imagePath && <img src={imagePath} alt={name} className="filter-button-image" />}
    <p>{name}</p>
  </button>
);

const App = () => {
  const [modData, setModData] = useState({ tools: [] });
  const [filters, setFilters] = useState({ stick: null, material: null, toolType: null });
  const [searchTerm, setSearchTerm] = useState('');
  const [activeTab, setActiveTab] = useState('all');
  const [error, setError] = useState(null);
  
  const [stickImages, setStickImages] = useState([]);
  const [materialImages, setMaterialImages] = useState([]);

  useEffect(() => {
    try {
      console.log('Loading mod data...');
      setModData(modItemsCatalog);
      setStickImages(modItemsCatalog.sticks);
      setMaterialImages(modItemsCatalog.materials);
      console.log('Mod data loaded!', modItemsCatalog);
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
      <h1>Fariance Mod Showcase</h1>
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
              {stickImages.map((stick) => (
                <FilterButton
                  key={stick.name}
                  name={stick.name.replace(' Stick', '')}
                  onClick={() => setFilters({ ...filters, stick: stick.id.toLowerCase() })}
                  isActive={filters.stick === stick.id.toLowerCase()}
                  imagePath={stick.imagePath}
                />
              ))}
            </div>
            <div className="tool-grid">
              {filteredTools.map((tool, index) => (
                <ToolCard
                  key={index}
                  imageSrc={tool.imagePath}
                  name={tool.name}
                  material={tool.material}
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
              {materialImages.map((material) => (
                <FilterButton
                  key={material.name}
                  name={material.name}
                  onClick={() => setFilters({ ...filters, material: material.id.toLowerCase() })}
                  isActive={filters.material === material.id.toLowerCase()}
                  imagePath={material.imagePath}
                />
              ))}
            </div>
            <div className="tool-grid">
              {filteredTools.map((tool, index) => (
                <ToolCard
                  key={index}
                  imageSrc={tool.imagePath}
                  name={tool.name}
                  material={tool.material}
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
