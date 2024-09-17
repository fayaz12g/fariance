package one.fayaz.woodstuff;

import net.minecraft.client.renderer.ItemBlockRenderTypes;
import net.minecraft.client.renderer.RenderType;
import net.minecraft.core.BlockPos;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.item.*;
import net.minecraft.world.level.LevelReader;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.block.LadderBlock;
import net.minecraft.world.level.block.SoundType;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.block.state.BlockState;
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
import java.util.List;

@Mod.EventBusSubscriber(modid = WoodStuffMod.MODID, bus = Mod.EventBusSubscriber.Bus.MOD)
public class ItemRegistry {
    private static final Logger LOGGER = LogUtils.getLogger();
    public static final DeferredRegister<Item> ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, WoodStuffMod.MODID);
    public static final DeferredRegister<Block> BLOCKS = DeferredRegister.create(ForgeRegistries.BLOCKS, WoodStuffMod.MODID);

    public static final Map<String, RegistryObject<Item>> GENERATED_ITEMS = new HashMap<>();
    public static final Map<String, RegistryObject<Block>> GENERATED_BLOCKS = new HashMap<>();

    private static final List<String> WOOD_TYPES = Arrays.asList("oak", "spruce", "birch", "jungle", "acacia", "dark_oak", "mangrove", "cherry", "crimson", "warped", "bamboo");
    private static final List<String> TOOL_TYPES = Arrays.asList("sword", "pickaxe", "shovel", "hoe", "axe");
    private static final List<String> MATERIAL_TYPES = Arrays.asList("oak", "spruce", "birch", "jungle", "acacia", "dark_oak", "mangrove", "cherry", "crimson", "warped", "bamboo",
            "iron", "diamond", "copper", "gold", "netherite", "amethyst", "diorite", "andesite", "granite", "blackstone", "cobblestone", "redstone", "lapis", "quartz", "deepslate");
    private static final List<String> STICK_TYPES = Arrays.asList("oak", "spruce", "birch", "jungle", "acacia", "dark_oak", "mangrove", "cherry", "crimson", "warped", "bamboo", "blaze", "breeze");

    static {
        generateTools();
        generateSticks();
        generateLadders();
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

    private static void generateSticks() {
        for (String stick : STICK_TYPES) {
            String stickName = stick + "_stick";
            GENERATED_ITEMS.put(stickName, ITEMS.register(stickName, () -> new Item(new Item.Properties())));
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
            case "sword": return new SwordItem(tier, new Item.Properties());
            case "pickaxe": return new PickaxeItem(tier, new Item.Properties());
            case "shovel": return new ShovelItem(tier, new Item.Properties());
            case "hoe": return new HoeItem(tier, new Item.Properties());
            case "axe": return new AxeItem(tier, new Item.Properties());
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