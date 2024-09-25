package one.fayaz.woodstuff;

import net.minecraft.client.renderer.ItemBlockRenderTypes;
import net.minecraft.client.renderer.RenderType;
import net.minecraft.core.BlockPos;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.item.*;
import net.minecraft.world.level.LevelReader;
import net.minecraft.world.level.block.*;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.material.MapColor;
import net.minecraft.world.level.block.SoundType;
import net.minecraftforge.fml.event.lifecycle.FMLClientSetupEvent;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.eventbus.api.IEventBus;
import org.slf4j.Logger;
import com.mojang.logging.LogUtils;

import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

@Mod.EventBusSubscriber(modid = WoodStuffMod.MODID, bus = Mod.EventBusSubscriber.Bus.MOD)
public class ItemRegistry {
    private static final Logger LOGGER = LogUtils.getLogger();
    public static final DeferredRegister<Item> ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, WoodStuffMod.MODID);
    public static final DeferredRegister<Block> BLOCKS = DeferredRegister.create(ForgeRegistries.BLOCKS, WoodStuffMod.MODID);

    public static final Map<String, RegistryObject<Item>> GENERATED_ITEMS = new HashMap<>();
    public static final Map<String, RegistryObject<Block>> GENERATED_BLOCKS = new HashMap<>();

    private static final List<String> WOOD_TYPES = Arrays.asList("oak", "spruce", "birch", "jungle", "acacia", "dark_oak", "mangrove", "cherry", "crimson", "warped", "bamboo");
    private static final List<String> TOOL_TYPES = Arrays.asList("sword", "pickaxe", "shovel", "hoe", "axe");

    private static final List<String> STONE_TYPES = Arrays.asList("cobblestone", "deepslate", "andesite", "diorite", "granite", "blackstone");

    private static final List<String> MATERIAL_TYPES = new ArrayList<>();
    static {
        MATERIAL_TYPES.addAll(Arrays.asList(
                "oak", "spruce", "birch", "jungle", "acacia", "dark_oak", "mangrove", "cherry", "crimson", "warped", "bamboo",
                "iron", "diamond", "gold", "netherite", "amethyst", "redstone", "lapis", "quartz", "prismarine",
                "shiny_copper", "weathered_copper", "exposed_copper", "oxidized_copper"
        ));
        // Add stone types dynamically
        MATERIAL_TYPES.addAll(STONE_TYPES);
    }

    private static final List<String> STICK_TYPES = Arrays.asList("oak", "spruce", "birch", "jungle", "acacia", "dark_oak", "mangrove", "cherry", "crimson", "warped", "bamboo", "blaze", "breeze");
    private static final List<String> STRIPPED_STICK_TYPES = WOOD_TYPES.stream().map(wood -> "stripped_" + wood).collect(Collectors.toList());

    static {
        generateTools();
        generateSticks();
        generateLadders();
        generateIngots();
        generateCraftingTables();
        generateFurnaces();
    }

    private static void generateTools() {
        for (String material : MATERIAL_TYPES) {
            for (String tool : TOOL_TYPES) {
                for (String stick : STICK_TYPES) {
                    String itemName = material + "_" + tool + "_with_" + stick + "_stick";
                    Tier tier = getTier(material);
                    GENERATED_ITEMS.put(itemName, ITEMS.register(itemName, () -> createTool(tool, tier)));
                }
                for (String strippedStick : STRIPPED_STICK_TYPES) {
                    String itemName = material + "_" + tool + "_with_" + strippedStick + "_stick";
                    Tier tier = getTier(material);
                    GENERATED_ITEMS.put(itemName, ITEMS.register(itemName, () -> createTool(tool, tier)));
                }
            }
        }
    }

    private static void generateSticks() {
        for (String stick : STICK_TYPES) {
            String stickName = stick + "_stick";
            GENERATED_ITEMS.put(stickName, ITEMS.register(stickName, () -> new Item(new Item.Properties())));
        }
        for (String strippedStick : STRIPPED_STICK_TYPES) {
            GENERATED_ITEMS.put(strippedStick, ITEMS.register(strippedStick, () -> new Item(new Item.Properties())));
        }
    }

    private static void generateLadders() {
        for (String wood : WOOD_TYPES) {
            String ladderName = wood + "_ladder";
            RegistryObject<Block> block = BLOCKS.register(ladderName, () -> createLadderBlock(wood));
            GENERATED_BLOCKS.put(ladderName, block);
            GENERATED_ITEMS.put(ladderName, ITEMS.register(ladderName, () -> new BlockItem(block.get(), new Item.Properties())));
        }
        // Special ladders
        generateSpecialLadder("blaze");
        generateSpecialLadder("breeze");
    }

    private static void generateIngots() {
        List<String> copperTypes = Arrays.asList("shiny_copper", "weathered_copper", "exposed_copper", "oxidized_copper");
        for (String copperType : copperTypes) {
            String ingotName = copperType + "_ingot";
            GENERATED_ITEMS.put(ingotName, ITEMS.register(ingotName, () -> new Item(new Item.Properties())));
        }
    }

    private static void generateCraftingTables() {
        for (String wood : WOOD_TYPES) {
            String tableName = wood + "_crafting_table";
            RegistryObject<Block> block = BLOCKS.register(tableName, () -> createCraftingTableBlock(wood));
            GENERATED_BLOCKS.put(tableName, block);
            GENERATED_ITEMS.put(tableName, ITEMS.register(tableName, () -> new BlockItem(block.get(), new Item.Properties())));
        }
    }

    private static void generateFurnaces() {
        for (String stone : STONE_TYPES) {
            String furnaceName = stone + "_furnace";
            RegistryObject<Block> block = BLOCKS.register(furnaceName, () -> createFurnaceBlock(stone));
            GENERATED_BLOCKS.put(furnaceName, block);
            GENERATED_ITEMS.put(furnaceName, ITEMS.register(furnaceName, () -> new BlockItem(block.get(), new Item.Properties())));
        }
    }

    private static Block createCraftingTableBlock(String wood) {
        return new CraftingTableBlock(BlockBehaviour.Properties.of()
                .mapColor(MapColor.WOOD)
                .strength(2.5F)
                .sound(SoundType.WOOD)
                .ignitedByLava()) {
            @Override
            public void onPlace(BlockState pState, net.minecraft.world.level.Level pLevel, BlockPos pPos, BlockState pOldState, boolean pIsMoving) {
                LOGGER.info("Placed " + wood + " crafting table at " + pPos);
            }
        };
    }

    private static Block createFurnaceBlock(String stone) {
        return new FurnaceBlock(BlockBehaviour.Properties.of()
                .mapColor(MapColor.STONE)
                .requiresCorrectToolForDrops()
                .strength(3.5F)
                .lightLevel(state -> state.getValue(FurnaceBlock.LIT) ? 13 : 0)) {
            @Override
            public void onPlace(BlockState pState, net.minecraft.world.level.Level pLevel, BlockPos pPos, BlockState pOldState, boolean pIsMoving) {
                LOGGER.info("Placed " + stone + " furnace at " + pPos);
            }
        };
    }

    private static void generateSpecialLadder(String material) {
        String ladderName = material + "_ladder";
        RegistryObject<Block> block = BLOCKS.register(ladderName, () -> createLadderBlock(material));
        GENERATED_BLOCKS.put(ladderName, block);
        GENERATED_ITEMS.put(ladderName, ITEMS.register(ladderName, () -> new BlockItem(block.get(), new Item.Properties())));
    }

    private static Tier getTier(String material) {
        if (WOOD_TYPES.contains(material)) return Tiers.WOOD;
        switch (material) {
            case "iron": return Tiers.IRON;
            case "diamond": return Tiers.DIAMOND;
            case "gold": return Tiers.GOLD;
            case "netherite": return Tiers.NETHERITE;
            case "shiny_copper":
            case "weathered_copper":
            case "exposed_copper":
            case "oxidized_copper":
                return Tiers.IRON; // Assuming copper tiers are similar to iron
            default: return Tiers.STONE;  // Default to STONE for custom materials
        }
    }

    private static Block createLadderBlock(String material) {
        return new LadderBlock(BlockBehaviour.Properties.of()
                .strength(0.4F)
                .sound(SoundType.LADDER)
                .noOcclusion()
                .noCollission()
                .ignitedByLava()) {
            @Override
            public boolean isLadder(BlockState state, LevelReader world, BlockPos pos, LivingEntity entity) {
                return true;
            }
        };
    }

    private static Item createTool(String tool, Tier tier) {
        switch (tool) {
            case "sword": return new SwordItem(tier,  new Item.Properties());
            case "pickaxe": return new PickaxeItem(tier,  new Item.Properties());
            case "shovel": return new ShovelItem(tier, new Item.Properties());
            case "hoe": return new HoeItem(tier,  new Item.Properties());
            case "axe": return new AxeItem(tier,  new Item.Properties());
            default: throw new IllegalArgumentException("Unknown tool type: " + tool);
        }
    }

    public static void register(IEventBus modEventBus) {
        ITEMS.register(modEventBus);
        BLOCKS.register(modEventBus);
        modEventBus.addListener(ItemRegistry::clientSetup);
    }

    public static void clientSetup(final FMLClientSetupEvent event) {
        event.enqueueWork(() -> {
            for (RegistryObject<Block> block : GENERATED_BLOCKS.values()) {
                ItemBlockRenderTypes.setRenderLayer(block.get(), RenderType.cutout());
            }
        });
    }
}