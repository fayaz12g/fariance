package one.fayaz.fariance;

import net.minecraft.client.renderer.ItemBlockRenderTypes;
import net.minecraft.client.renderer.RenderType;
import net.minecraft.core.BlockPos;
import net.minecraft.core.particles.ParticleOptions;
import net.minecraft.core.particles.ParticleTypes;
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
import net.minecraft.world.level.block.state.properties.BlockSetType;
import net.minecraft.world.level.block.state.properties.WoodType;
import net.minecraft.world.level.material.FlowingFluid;
import net.minecraft.world.level.material.MapColor;
import net.minecraft.world.level.block.SoundType;
import net.minecraft.world.phys.BlockHitResult;
import net.minecraftforge.fml.event.lifecycle.FMLClientSetupEvent;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.eventbus.api.IEventBus;
import one.fayaz.fariance.blocks.*;
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

    private static final List<String> POTION_TYPES = Arrays.asList(
            "mundane", "thick", "awkward", "night_vision", "invisibility", "leaping",
            "fire_resistance", "swiftness", "slowness", "turtle_master", "water_breathing",
            "healing", "harming", "poison", "regeneration", "strength", "weakness", "luck",
            "slow_falling"
    );

    private static final List<String> TORCH_TYPES = Arrays.asList(
            "normal", "redstone", "soul");

    private static final List<String> NEW_WOOD_TYPES = Arrays.asList(
            "pale_oak", "charred", "tyrian", "azalea");

    private static final List<String> NETHER_WOODS = Arrays.asList(
            "crimson", "charred", "tyrian", "warped");


    private static final List<String> WOOD_TYPES = new ArrayList<>();
    static {
        WOOD_TYPES.addAll(Arrays.asList("oak", "spruce", "birch", "jungle", "acacia", "dark_oak", "mangrove", "cherry", "crimson", "warped", "bamboo"));
        WOOD_TYPES.addAll(NEW_WOOD_TYPES);
    }
    private static final List<String> TOOL_TYPES = Arrays.asList(
            "sword", "pickaxe", "shovel", "hoe", "axe");

    private static final List<String> MATERIAL_BASE = Arrays.asList(
            "iron", "diamond", "gold", "netherite");

    private static final List<String> MATERIAL_NEW = Arrays.asList(
            "amethyst", "redstone", "lapis", "quartz");

    private static final List<String> STONE_TYPES = Arrays.asList(
            "cobblestone", "deepslate", "andesite", "diorite", "granite", "blackstone", "prismarine", "sandstone", "red_sandstone", "end_stone", "tuff");

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

    private static final List<String> WOOL_TYPES = Arrays.asList(
            "black", "blue", "brown", "cyan", "gray", "green", "light_blue", "light_gray",
            "lime", "magenta", "orange", "pink", "purple", "red", "white", "yellow"
    );

    public static final Map<String, RegistryObject<Item>> POTION_BUCKETS = new HashMap<>();
    public static final Map<String, RegistryObject<LiquidBlock>> POTION_FLUIDS = new HashMap<>();
    public static final Map<String, RegistryObject<FlowingFluid>> POTION_FLUID_SOURCES = new HashMap<>();
    public static final Map<String, RegistryObject<FlowingFluid>> POTION_FLUID_FLOWINGS = new HashMap<>();


    static {
        generateTools();
        generateSticks();
        generateLadders();
        generateIngots();
        generateCraftingTables();
        generateFurnaces();
        generateShields();
        generatePotionBucketsAndFluids();
        generateBeds();
        generateNewWoodBlocks();
        generateTorches();
    }

    private static void generateTorches() {
        for (String wood : STICK_TYPES) {
            if (!wood.equals("breeze") && !wood.equals("blaze")) {
                final String woodName = wood;

                // Normal Torch
                createTorchSet(woodName, "", ParticleTypes.FLAME, 14);

                // Soul Torch
                createTorchSet(woodName, "soul_", ParticleTypes.SOUL_FIRE_FLAME, 10);

                // Redstone Torch
                createRedstoneTorchSet(woodName);
            }
        }
    }

    private static void createTorchSet(String woodName, String prefix, ParticleOptions particleType, int lightLevel) {
        // Wall Torch (register first)
        RegistryObject<Block> wallTorch = BLOCKS.register(woodName + "_" + prefix + "wall_torch",
                () -> new CustomWallTorchBlock(
                        particleType,
                        BlockBehaviour.Properties.of()
                                .mapColor(MapColor.WOOD)
                                .noCollission()
                                .strength(0.5F)
                                .sound(SoundType.WOOD)
                                .lightLevel((state) -> lightLevel)));

        // Torch (upright placement)
        RegistryObject<Block> torch = BLOCKS.register(woodName + "_" + prefix + "torch",
                () -> new CustomTorchBlock(
                        particleType,
                        BlockBehaviour.Properties.of()
                                .mapColor(MapColor.WOOD)
                                .noCollission()
                                .strength(0.5F)
                                .sound(SoundType.WOOD)
                                .lightLevel((state) -> lightLevel),
                        wallTorch.get()));

        // Add both torch and wall torch to the GENERATED_BLOCKS map
        GENERATED_BLOCKS.put(woodName + "_" + prefix + "torch", torch);
        GENERATED_BLOCKS.put(woodName + "_" + prefix + "wall_torch", wallTorch);

        // Register block item for the torch (will handle both placements)
        registerBlockItem(woodName + "_" + prefix + "torch", torch);
    }

    private static void createRedstoneTorchSet(String woodName) {
        // Redstone Wall Torch (register first)
        RegistryObject<Block> redstoneWallTorch = BLOCKS.register(woodName + "_redstone_wall_torch",
                () -> new CustomRedstoneWallTorchBlock(
                        BlockBehaviour.Properties.of()
                                .mapColor(MapColor.WOOD)
                                .noCollission()
                                .strength(0.5F)
                                .sound(SoundType.WOOD)
                                .lightLevel((state) -> state.getValue(RedstoneWallTorchBlock.LIT) ? 7 : 0)));

        // Redstone Torch (upright placement)
        RegistryObject<Block> redstoneTorch = BLOCKS.register(woodName + "_redstone_torch",
                () -> new CustomRedstoneTorchBlock(
                        BlockBehaviour.Properties.of()
                                .mapColor(MapColor.WOOD)
                                .noCollission()
                                .strength(0.5F)
                                .sound(SoundType.WOOD)
                                .lightLevel((state) -> state.getValue(RedstoneTorchBlock.LIT) ? 7 : 0),
                        redstoneWallTorch.get()));

        // Add both redstone torch and wall torch to the GENERATED_BLOCKS map
        GENERATED_BLOCKS.put(woodName + "_redstone_torch", redstoneTorch);
        GENERATED_BLOCKS.put(woodName + "_redstone_wall_torch", redstoneWallTorch);

        // Register block item for the redstone torch (will handle both placements)
        registerBlockItem(woodName + "_redstone_torch", redstoneTorch);
    }

    private static void generateNewWoodBlocks() {
        for (String wood : NEW_WOOD_TYPES) {
            final String woodName = wood; // Create a final copy for use in lambdas

            // Plank
            RegistryObject<Block> planks = BLOCKS.register(woodName + "_planks",
                    () -> new Block(BlockBehaviour.Properties.of().strength(2.0F, 3.0F).sound(SoundType.WOOD)));
            GENERATED_BLOCKS.put(woodName + "_planks", planks);
            registerBlockItem(woodName + "_planks", planks);

            // Pressure Plate
            RegistryObject<Block> pressurePlate = BLOCKS.register(woodName + "_pressure_plate",
                    () -> new PressurePlateBlock(BlockSetType.OAK, BlockBehaviour.Properties.of().mapColor(MapColor.WOOD).noCollission().strength(0.5F).sound(SoundType.WOOD)));
            GENERATED_BLOCKS.put(woodName + "_pressure_plate", pressurePlate);
            registerBlockItem(woodName + "_pressure_plate", pressurePlate);

            // Button
            RegistryObject<Block> button = BLOCKS.register(woodName + "_button",
                    () -> new ButtonBlock(BlockSetType.OAK, 30, BlockBehaviour.Properties.of().noCollission().strength(0.5F).sound(SoundType.WOOD)));
            GENERATED_BLOCKS.put(woodName + "_button", button);
            registerBlockItem(woodName + "_button", button);

            // Fence Gate
            RegistryObject<Block> fenceGate = BLOCKS.register(woodName + "_fence_gate",
                    () -> new FenceGateBlock(WoodType.OAK, BlockBehaviour.Properties.of().strength(2.0F, 3.0F).sound(SoundType.WOOD)));
            GENERATED_BLOCKS.put(woodName + "_fence_gate", fenceGate);
            registerBlockItem(woodName + "_fence_gate", fenceGate);

            // Fence
            RegistryObject<Block> fence = BLOCKS.register(woodName + "_fence",
                    () -> new CustomFenceBlock(BlockBehaviour.Properties.of().strength(2.0F, 3.0F).sound(SoundType.WOOD)));
            GENERATED_BLOCKS.put(woodName + "_fence", fence);
            registerBlockItem(woodName + "_fence", fence);

            // Door
            RegistryObject<Block> door = BLOCKS.register(woodName + "_door",
                    () -> new DoorBlock(BlockSetType.OAK, BlockBehaviour.Properties.of().strength(3.0F).sound(SoundType.WOOD).noOcclusion()));
            GENERATED_BLOCKS.put(woodName + "_door", door);
            registerBlockItem(woodName + "_door", door);

            String log_type = "_log";
            if (NETHER_WOODS.contains(wood)) {
                log_type = "_stem";
            }

            // Log or Stem
            RegistryObject<Block> stem = BLOCKS.register(woodName + log_type,
                    () -> new RotatedPillarBlock(BlockBehaviour.Properties.of().strength(2.0F).sound(SoundType.WOOD)));
            GENERATED_BLOCKS.put(woodName + log_type, stem);
            registerBlockItem(woodName + log_type, stem);

            // Stripped Log or Stem
            RegistryObject<Block> strippedStem = BLOCKS.register("stripped_" + woodName + log_type,
                    () -> new RotatedPillarBlock(BlockBehaviour.Properties.of().strength(2.0F).sound(SoundType.WOOD)));
            GENERATED_BLOCKS.put("stripped_" + woodName + log_type, strippedStem);
            registerBlockItem("stripped_" + woodName + log_type, strippedStem);


            // Slab
            RegistryObject<Block> slab = BLOCKS.register(woodName + "_slab",
                    () -> new SlabBlock(BlockBehaviour.Properties.of().strength(2.0F, 3.0F).sound(SoundType.WOOD)));
            GENERATED_BLOCKS.put(woodName + "_slab", slab);
            registerBlockItem(woodName + "_slab", slab);

//             // Stair (broken)
//            RegistryObject<Block> stair = BLOCKS.register(woodName + "_stairs",
//                    () -> new StairBlock(() -> GENERATED_BLOCKS.get(woodName + "_planks").get().defaultBlockState(),
//                            BlockBehaviour.Properties.of().strength(2.0F, 3.0F).sound(SoundType.WOOD)));
//            GENERATED_BLOCKS.put(woodName + "_stairs", stair);
//            registerBlockItem(woodName + "_stairs", stair);
//
            // Trapdoor
            RegistryObject<Block> trapdoor = BLOCKS.register(woodName + "_trapdoor",
                    () -> new TrapDoorBlock(BlockSetType.OAK, BlockBehaviour.Properties.of().strength(3.0F).sound(SoundType.WOOD).noOcclusion()));
            GENERATED_BLOCKS.put(woodName + "_trapdoor", trapdoor);
            registerBlockItem(woodName + "_trapdoor", trapdoor);
//
            // Sign
            RegistryObject<Block> sign = BLOCKS.register(woodName + "_sign",
                    () -> new StandingSignBlock(WoodType.OAK, BlockBehaviour.Properties.of().noCollission().strength(1.0F).sound(SoundType.WOOD)));
            GENERATED_BLOCKS.put(woodName + "_sign", sign);
            registerBlockItem(woodName + "_sign", sign);
//
            // Wall Sign
            RegistryObject<Block> wallSign = BLOCKS.register(woodName + "_wall_sign",
                    () -> new WallSignBlock(WoodType.OAK, BlockBehaviour.Properties.of().noCollission().strength(1.0F).sound(SoundType.WOOD)));
            GENERATED_BLOCKS.put(woodName + "_wall_sign", wallSign);
            // Note: We don't register an item for the wall sign as it uses the same item as the standing sign
//
            // Hanging Sign
            RegistryObject<Block> hangingSign = BLOCKS.register(woodName + "_hanging_sign",
                    () -> new CeilingHangingSignBlock(WoodType.OAK, BlockBehaviour.Properties.of().noCollission().strength(1.0F).sound(SoundType.WOOD)));
            GENERATED_BLOCKS.put(woodName + "_hanging_sign", hangingSign);
            registerBlockItem(woodName + "_hanging_sign", hangingSign);
//
            // Wall Hanging Sign
            RegistryObject<Block> wallHangingSign = BLOCKS.register(woodName + "_wall_hanging_sign",
                    () -> new WallHangingSignBlock(WoodType.OAK, BlockBehaviour.Properties.of().noCollission().strength(1.0F).sound(SoundType.WOOD)));
            GENERATED_BLOCKS.put(woodName + "_wall_hanging_sign", wallHangingSign);
            // Note: We don't register an item for the wall hanging sign as it uses the same item as the ceiling hanging sign
//
//            // Boat (broken)
//            if (!NETHER_WOODS.contains(wood)) {
//                RegistryObject<Item> boat = ITEMS.register(woodName + "_boat",
//                        () -> new BoatItem(false, new Item.Properties().stacksTo(1)));
//                GENERATED_ITEMS.put(woodName + "_boat", boat);
//
//                RegistryObject<Item> chestBoat = ITEMS.register(woodName + "_chest_boat",
//                        () -> new BoatItem(true, new Item.Properties().stacksTo(1)));
//                GENERATED_ITEMS.put(woodName + "_chest_boat", chestBoat);
//            }

        }
    }

    // Helper method to register BlockItems
    private static void registerBlockItem(String name, RegistryObject<Block> block) {
        GENERATED_ITEMS.put(name, ITEMS.register(name, () -> new BlockItem(block.get(), new Item.Properties())));
    }


    // BEDS
    private static void generateBeds() {
        for (String wood : WOOD_TYPES) {
            for (String wool : WOOL_TYPES) {
                String bedName = wood + "_" + wool + "_bed";
                RegistryObject<Block> block = BLOCKS.register(bedName, () -> createBedBlock(wood, wool));
                GENERATED_BLOCKS.put(bedName, block);
                GENERATED_ITEMS.put(bedName, ITEMS.register(bedName, () -> new BedItem(block.get(), new Item.Properties())));
            }
        }
    }

    private static Block createBedBlock(String wood, String wool) {
        DyeColor color = DyeColor.valueOf(wool.toUpperCase());
        return new CustomBedBlock(color, BlockBehaviour.Properties.of()
                .mapColor(MapColor.WOOD)
                .sound(SoundType.WOOD)
                .strength(0.2F)
                .noOcclusion());
    }

    private static DyeColor getDyeColor(String wool) {
        return DyeColor.valueOf(wool.toUpperCase());
    }

    // POTIONS
    private static void generatePotionBucketsAndFluids() {
        for (String potionType : POTION_TYPES) {
//            registerPotionFluid(potionType);
//            registerPotionBucket(potionType);
        }
    }


    // TOOLS
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
            // Exclude "blaze", "breeze", and "bamboo" from stick generation
            if (!stick.equals("blaze") && !stick.equals("breeze") && !stick.equals("bamboo")) {
                String stickName = stick + "_stick";
                GENERATED_ITEMS.put(stickName, ITEMS.register(stickName, () -> new Item(new Item.Properties())));
            }
        }
    }

    // LADDERS
    private static void generateLadders() {
        for (String wood : STICK_TYPES) {
            String ladderName = wood + "_ladder";
            RegistryObject<Block> block = BLOCKS.register(ladderName, () -> createLadderBlock(wood));
            GENERATED_BLOCKS.put(ladderName, block);
            GENERATED_ITEMS.put(ladderName, ITEMS.register(ladderName, () -> new BlockItem(block.get(), new Item.Properties())));
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
            RegistryObject<Block> block = BLOCKS.register(furnaceName, () -> createFurnaceBlock(stone));
            GENERATED_BLOCKS.put(furnaceName, block);
            GENERATED_ITEMS.put(furnaceName, ITEMS.register(furnaceName, () -> new BlockItem(block.get(), new Item.Properties())));
        }
    }

    private static Block createFurnaceBlock(String stone) {
        return new CustomFurnaceBlock(BlockBehaviour.Properties.of()
                .mapColor(MapColor.STONE)
                .requiresCorrectToolForDrops()
                .strength(3.5F)
                .lightLevel(state -> state.getValue(FurnaceBlock.LIT) ? 13 : 0)) {
        };
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