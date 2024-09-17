package one.fayaz.woodstuff;

import com.mojang.logging.LogUtils;
import net.minecraft.core.registries.Registries;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.CreativeModeTabs;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.material.MapColor;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.event.BuildCreativeModeTabContentsEvent;
import net.minecraftforge.event.server.ServerStartingEvent;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.config.ModConfig;
import net.minecraftforge.fml.event.lifecycle.FMLClientSetupEvent;
import net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.RegistryObject;
import org.slf4j.Logger;

// The value here should match an entry in the META-INF/mods.toml file
@Mod(WoodStuffMod.MODID)
public class WoodStuffMod {
    public static final String MODID = "woodstuff";
    private static final Logger LOGGER = LogUtils.getLogger();

    // Create a Deferred Register to hold Items which will all be registered under the "woodstuff" namespace
    public static final DeferredRegister<Item> ITEMS = DeferredRegister.create(Registries.ITEM, MODID);
    // Create a Deferred Register to hold CreativeModeTabs which will all be registered under the "woodstuff" namespace
    public static final DeferredRegister<CreativeModeTab> CREATIVE_MODE_TABS = DeferredRegister.create(Registries.CREATIVE_MODE_TAB, MODID);

    // Register your items
    public static final ItemRegistry ItemRegistry = new ItemRegistry();

    // Create a new CreativeModeTab
    public static final RegistryObject<CreativeModeTab> WOODSTUFF_TAB = CREATIVE_MODE_TABS.register("woodstuff_tab", () -> CreativeModeTab.builder()
            .withTabsBefore(CreativeModeTabs.BUILDING_BLOCKS)
            .icon(() -> ItemRegistry.GENERATED_ITEMS.get("oak_sword_with_oak_stick").get().getDefaultInstance())
            .displayItems((parameters, output) -> {
                // Add all items from the generated items to the creative tab
                ItemRegistry.GENERATED_ITEMS.values().forEach(itemRegistryObject -> output.accept(itemRegistryObject.get()));
            }).build());

    public WoodStuffMod(FMLJavaModLoadingContext context) {
        IEventBus modEventBus = context.getModEventBus();

        // Register the commonSetup method for modloading
        modEventBus.addListener(this::commonSetup);

        // Register the Deferred Register to the mod event bus
        ItemRegistry.register(modEventBus);
        CREATIVE_MODE_TABS.register(modEventBus);

        // Register ourselves for server and other game events
        MinecraftForge.EVENT_BUS.register(this);
    }

    private void commonSetup(final FMLCommonSetupEvent event) {
        // Some common setup code
        LOGGER.info("HELLO FROM COMMON SETUP");
    }
}
