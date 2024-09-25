package one.fayaz.fariance;

import net.minecraft.client.renderer.ItemBlockRenderTypes;
import net.minecraft.client.renderer.RenderType;
import net.minecraft.core.BlockPos;
import net.minecraft.core.Direction;
import net.minecraft.network.chat.Component;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.InteractionResult;
import net.minecraft.world.MenuProvider;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.inventory.ContainerLevelAccess;
import net.minecraft.world.item.*;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.LevelReader;
import net.minecraft.world.level.block.*;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.block.state.StateDefinition;
import net.minecraft.world.level.block.state.properties.BooleanProperty;
import net.minecraft.world.level.block.state.properties.DirectionProperty;
import net.minecraft.world.level.material.MapColor;
import net.minecraft.world.level.block.SoundType;
import net.minecraft.world.phys.BlockHitResult;
import net.minecraftforge.fml.event.lifecycle.FMLClientSetupEvent;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.eventbus.api.IEventBus;
import org.slf4j.Logger;
import net.minecraft.world.inventory.AbstractContainerMenu;
import net.minecraft.world.entity.player.Inventory;
import com.mojang.logging.LogUtils;

import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

@Mod.EventBusSubscriber(modid = FarianceMod.MODID, bus = Mod.EventBusSubscriber.Bus.MOD)
public class ItemRegistry {
    private static final Logger LOGGER = LogUtils.getLogger();
    public static final DeferredRegister<Item> ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, FarianceMod.MODID);
    public static final DeferredRegister<Block> BLOCKS = DeferredRegister.create(ForgeRegistries.BLOCKS, FarianceMod.MODID);

    public static final Map<String, RegistryObject<Item>> GENERATED_ITEMS = new HashMap<>();
    public static final Map<String, RegistryObject<Block>> GENERATED_BLOCKS = new HashMap<>();

    private static final List<String> WOOD_TYPES = Arrays.asList(
            "oak", "spruce", "birch", "jungle", "acacia", "dark_oak", "mangrove", "cherry", "crimson", "warped", "bamboo");

    private static final List<String> TOOL_TYPES = Arrays.asList(
            "sword", "pickaxe", "shovel", "hoe", "axe");

    private static final List<String> MATERIAL_BASE = Arrays.asList(
            "iron", "diamond", "gold", "netherite");

    private static final List<String> MATERIAL_NEW = Arrays.asList(
            "amethyst", "redstone", "lapis", "quartz");

    private static final List<String> STONE_TYPES = Arrays.asList(
            "cobblestone", "deepslate", "andesite", "diorite", "granite", "blackstone", "prismarine");

    private static final List<String> COPPER_TYPES = Arrays.asList(
            "shiny_copper", "weathered_copper", "exposed_copper", "oxidized_copper");

    private static final List<String> STICK_TYPES = new ArrayList<>();
    static {
        STICK_TYPES.addAll(Arrays.asList("blaze", "breeze")); // Add base stick types
        STICK_TYPES.addAll(WOOD_TYPES); // Add wood types
        STICK_TYPES.addAll(WOOD_TYPES.stream().map(wood -> "stripped_" + wood).collect(Collectors.toList())); // Add stripped wood types
    }

    private static final List<String> MATERIAL_TYPES = new ArrayList<>();
    static {
        MATERIAL_TYPES.addAll(MATERIAL_BASE);
        MATERIAL_TYPES.addAll(STONE_TYPES);
        MATERIAL_TYPES.addAll(MATERIAL_NEW);
        MATERIAL_TYPES.addAll(COPPER_TYPES);
        MATERIAL_TYPES.addAll(WOOD_TYPES);
    }

    static {
        generateTools();
        generateSticks();
        generateLadders();
        generateIngots();
        generateCraftingTables();
        generateFurnaces();
        generateShields();
    }

    private static void generateTools() {
        for (String material : MATERIAL_TYPES) {
            for (String tool : TOOL_TYPES) {
                for (String stick : STICK_TYPES) {
                    String itemName = material + "_" + tool + "_with_" + stick + "_stick";
                    Tier tier = getTier(material);
                    GENERATED_ITEMS.put(itemName, ITEMS.register(itemName, () -> createTool(tool, tier)));
                }
            }
        }
    }

    // SHIELDS
    private static void generateShields() {
        for (String wood : WOOD_TYPES) {
            for (String material : MATERIAL_BASE) {
                String shieldName = wood + "_" + material + "_shield";
                GENERATED_ITEMS.put(shieldName, ITEMS.register(shieldName, () -> createShield(material)));
            }
        }
    }

    private static Item createShield(String material) {
        return new ShieldItem(new Item.Properties().durability(getDurability(material))) {
            @Override
            public boolean isValidRepairItem(ItemStack toRepair, ItemStack repair) {
                // Define repair items based on the material
                return getRepairMaterial(material).test(repair) || super.isValidRepairItem(toRepair, repair);
            }
        };
    }

    private static int getDurability(String material) {
        switch (material) {
            case "iron": return 336;
            case "diamond": return 672;
            case "gold": return 112;
            case "netherite": return 1008;
            default: return 336; // Default to iron durability
        }
    }

    private static java.util.function.Predicate<ItemStack> getRepairMaterial(String material) {
        switch (material) {
            case "iron": return (stack) -> stack.is(Items.IRON_INGOT);
            case "diamond": return (stack) -> stack.is(Items.DIAMOND);
            case "gold": return (stack) -> stack.is(Items.GOLD_INGOT);
            case "netherite": return (stack) -> stack.is(Items.NETHERITE_INGOT);
            default: return (stack) -> false;
        }
    }

    // STICKS
    private static void generateSticks() {
        for (String stick : STICK_TYPES) {
            String stickName = stick + "_stick";
            GENERATED_ITEMS.put(stickName, ITEMS.register(stickName, () -> new Item(new Item.Properties())));
        }
    }

    // LADDERS
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

    private static void generateSpecialLadder(String material) {
        String ladderName = material + "_ladder";
        RegistryObject<Block> block = BLOCKS.register(ladderName, () -> createLadderBlock(material));
        GENERATED_BLOCKS.put(ladderName, block);
        GENERATED_ITEMS.put(ladderName, ITEMS.register(ladderName, () -> new BlockItem(block.get(), new Item.Properties())));
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

    // COPPER INGOTS
    private static void generateIngots() {
        for (String copperType : COPPER_TYPES) {
            String ingotName = copperType + "_ingot";
            GENERATED_ITEMS.put(ingotName, ITEMS.register(ingotName, () -> new Item(new Item.Properties())));
        }
    }

    // FURNACES
    private static void generateFurnaces() {
        for (String stone : STONE_TYPES) {
            String furnaceName = stone + "_furnace";
            RegistryObject<Block> block = BLOCKS.register(furnaceName, () -> createDummyBlock(stone));
            GENERATED_BLOCKS.put(furnaceName, block);
            GENERATED_ITEMS.put(furnaceName, ITEMS.register(furnaceName, () -> new BlockItem(block.get(), new Item.Properties())));
        }
    }

    public static Block createDummyBlock(String stone) {
        // Create the block with properties
        Block block = new Block(BlockBehaviour.Properties.of()
                .mapColor(MapColor.STONE)
                .strength(1.5F)) {

            // Define block state properties
            public static final DirectionProperty FACING = DirectionProperty.create("facing");
            public static final BooleanProperty LIT = BooleanProperty.create("lit");

            // Constructor to set default block states
            {
                // Set the default block state to face north and be unlit
                this.registerDefaultState(this.stateDefinition.any()
                        .setValue(FACING, Direction.NORTH)
                        .setValue(LIT, false));
            }

            // Handle right-click behavior
            public InteractionResult use(BlockState state, Level level, BlockPos pos, Player player, InteractionHand hand, BlockHitResult hit) {
                // Toggle the 'lit' state
                boolean lit = !state.getValue(LIT);
                level.setBlock(pos, state.setValue(LIT, lit), 3);
                return InteractionResult.SUCCESS; // Indicate successful interaction
            }

            @Override
            public void onPlace(BlockState state, Level level, BlockPos pos, BlockState oldState, boolean isMoving) {
                LOGGER.info("Placed " + stone + " dummy block at " + pos);
            }

            @Override
            protected void createBlockStateDefinition(StateDefinition.Builder<Block, BlockState> builder) {
                builder.add(FACING, LIT);
            }
        };

        return block;
    }

    // CRAFTING TABLES
    private static void generateCraftingTables() {
        for (String wood : WOOD_TYPES) {
            String tableName = wood + "_crafting_table";
            RegistryObject<Block> block = BLOCKS.register(tableName, () -> createCraftingTableBlock(wood));
            GENERATED_BLOCKS.put(tableName, block);
            GENERATED_ITEMS.put(tableName, ITEMS.register(tableName, () -> new BlockItem(block.get(), new Item.Properties())));
        }
    }

    private static Block createCraftingTableBlock(String wood) {
        return new CraftingTableBlock(BlockBehaviour.Properties.of()
                .mapColor(MapColor.WOOD)
                .strength(2.5F)
                .sound(SoundType.WOOD)
                .ignitedByLava()) {

            @Override
            public MenuProvider getMenuProvider(BlockState state, Level level, BlockPos pos) {
                return new MenuProvider() {
                    @Override
                    public Component getDisplayName() {
                        return Component.translatable("container.crafting");
                    }

                    @Override
                    public AbstractContainerMenu createMenu(int windowId, Inventory playerInventory, Player player) {
                        // Use the CustomCraftingMenu instead of the vanilla one
                        return new CustomCraftingMenu(windowId, playerInventory, ContainerLevelAccess.create(level, pos));
                    }
                };
            }

            public InteractionResult use(BlockState state, Level level, BlockPos pos, Player player, InteractionHand hand, BlockHitResult hit) {
                if (level.isClientSide) {
                    return InteractionResult.SUCCESS; // Handle client-side interaction
                } else {
                    MenuProvider menuProvider = state.getMenuProvider(level, pos);
                    if (menuProvider != null) {
                        player.openMenu(menuProvider); // Open the menu on the server side
                    }
                    return InteractionResult.CONSUME; // Consume the interaction
                }
            }

            @Override
            public void onPlace(BlockState pState, Level pLevel, BlockPos pPos, BlockState pOldState, boolean pIsMoving) {
                LOGGER.info("Placed " + wood + " crafting table at " + pPos);
            }
        };
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