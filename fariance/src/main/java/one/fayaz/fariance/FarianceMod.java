package one.fayaz.fariance;

import com.mojang.logging.LogUtils;
import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.CreativeModeTabs;
import net.minecraft.world.item.Item;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.RegistryObject;
import one.fayaz.fariance.blocks.CustomBarrelBlock;
import one.fayaz.fariance.blocks.CustomBedBlock;
import one.fayaz.fariance.blocks.CustomFurnaceBlock;
import one.fayaz.fariance.blocks.signs.CustomSignBlockEntity;
import org.slf4j.Logger;

import java.util.List;
import java.util.stream.Collectors;

@Mod(FarianceMod.MODID)
public class FarianceMod {
    public static final String MODID = "fariance";
    private static final Logger LOGGER = LogUtils.getLogger();

    // Create Deferred Registers for Items and CreativeModeTabs
    public static final DeferredRegister<Item> ITEMS = DeferredRegister.create(Registries.ITEM, MODID);
    public static final DeferredRegister<CreativeModeTab> CREATIVE_MODE_TABS = DeferredRegister.create(Registries.CREATIVE_MODE_TAB, MODID);

    // Register the items from ItemRegistry
    public static final ItemRegistry ItemRegistry = new ItemRegistry();

    // Create CreativeModeTabs for each tool type
    public static final RegistryObject<CreativeModeTab> SWORDS_TAB = CREATIVE_MODE_TABS.register("swords_tab", () -> CreativeModeTab.builder()
            .withTabsBefore(CreativeModeTabs.SPAWN_EGGS)
            .icon(() -> ItemRegistry.GENERATED_ITEMS.get("blackstone_sword_with_stripped_crimson_stick").get().getDefaultInstance())
            .title(Component.translatable("itemGroup.fariance.swords"))
            .displayItems((parameters, output) -> addItemsToTab(output, "sword"))
            .build());

    public static final RegistryObject<CreativeModeTab> PICKAXES_TAB = CREATIVE_MODE_TABS.register("pickaxes_tab", () -> CreativeModeTab.builder()
            .withTabsBefore(CreativeModeTabs.SPAWN_EGGS)
            .icon(() -> ItemRegistry.GENERATED_ITEMS.get("blackstone_pickaxe_with_stripped_crimson_stick").get().getDefaultInstance())
            .title(Component.translatable("itemGroup.fariance.pickaxes"))
            .displayItems((parameters, output) -> addItemsToTab(output, "pickaxe"))
            .build());

    public static final RegistryObject<CreativeModeTab> AXES_TAB = CREATIVE_MODE_TABS.register("axes_tab", () -> CreativeModeTab.builder()
            .withTabsBefore(CreativeModeTabs.SPAWN_EGGS)
            .icon(() -> ItemRegistry.GENERATED_ITEMS.get("blackstone_axe_with_stripped_crimson_stick").get().getDefaultInstance())
            .title(Component.translatable("itemGroup.fariance.axes"))
            .displayItems((parameters, output) -> addItemsToTab(output, "axe"))
            .build());

    public static final RegistryObject<CreativeModeTab> SHOVELS_TAB = CREATIVE_MODE_TABS.register("shovels_tab", () -> CreativeModeTab.builder()
            .withTabsBefore(CreativeModeTabs.SPAWN_EGGS)
            .icon(() -> ItemRegistry.GENERATED_ITEMS.get("blackstone_shovel_with_stripped_crimson_stick").get().getDefaultInstance())
            .title(Component.translatable("itemGroup.fariance.shovels"))
            .displayItems((parameters, output) -> addItemsToTab(output, "shovel"))
            .build());

    public static final RegistryObject<CreativeModeTab> HOES_TAB = CREATIVE_MODE_TABS.register("hoes_tab", () -> CreativeModeTab.builder()
            .withTabsBefore(CreativeModeTabs.SPAWN_EGGS)
            .icon(() -> ItemRegistry.GENERATED_ITEMS.get("blackstone_hoe_with_stripped_crimson_stick").get().getDefaultInstance())
            .title(Component.translatable("itemGroup.fariance.hoes"))
            .displayItems((parameters, output) -> addItemsToTab(output, "hoe"))
            .build());

    public static final RegistryObject<CreativeModeTab> BEDS_TAB = CREATIVE_MODE_TABS.register("beds_tab", () -> CreativeModeTab.builder()
            .withTabsBefore(CreativeModeTabs.SPAWN_EGGS)
            .icon(() -> ItemRegistry.GENERATED_ITEMS.get("oak_red_bed").get().getDefaultInstance())
            .title(Component.translatable("itemGroup.fariance.beds"))
            .displayItems((parameters, output) -> addOtherItemsToTab(output, "bed"))
            .build());

    public static final RegistryObject<CreativeModeTab> SHIELDS_TAB = CREATIVE_MODE_TABS.register("shields_tab", () -> CreativeModeTab.builder()
            .withTabsBefore(CreativeModeTabs.SPAWN_EGGS)
            .icon(() -> ItemRegistry.GENERATED_ITEMS.get("oak_iron_shield").get().getDefaultInstance())
            .title(Component.translatable("itemGroup.fariance.shields"))
            .displayItems((parameters, output) -> addOtherItemsToTab(output, "shield"))
            .build());

    public static final RegistryObject<CreativeModeTab> TORCHES_TAB = CREATIVE_MODE_TABS.register("torches_tab", () -> CreativeModeTab.builder()
            .withTabsBefore(CreativeModeTabs.SPAWN_EGGS)
            .icon(() -> ItemRegistry.GENERATED_ITEMS.get("stripped_oak_torch").get().getDefaultInstance())
            .title(Component.translatable("itemGroup.fariance.torches"))
            .displayItems((parameters, output) -> addOtherItemsToTab(output, "torch"))
            .build());

    // New Misc tab for all other items
    public static final RegistryObject<CreativeModeTab> MISC_TAB = CREATIVE_MODE_TABS.register("misc_tab", () -> CreativeModeTab.builder()
            .withTabsBefore(CreativeModeTabs.SPAWN_EGGS)
            .icon(() -> ItemRegistry.GENERATED_ITEMS.get("charred_crafting_table").get().getDefaultInstance())
            .title(Component.translatable("itemGroup.fariance.misc"))
            .displayItems((parameters, output) -> addMiscItemsToTab(output))
            .build());

    public FarianceMod(FMLJavaModLoadingContext context) {
        IEventBus modEventBus = context.getModEventBus();

        // Register the commonSetup method for modloading
        modEventBus.addListener(this::commonSetup);

        // Register the Deferred Register to the mod event bus
        ItemRegistry.register(modEventBus);

        // Register the custom block entities
        CustomFurnaceBlock.registerBlockEntities();

        // Then register bed entities
        CustomBedBlock.registerBlockEntities();

        // Then register barrel entities
        CustomBarrelBlock.registerBlockEntities();

        // Register custom creative tabs
        CREATIVE_MODE_TABS.register(modEventBus);

        // Register ourselves for server and other game events
        MinecraftForge.EVENT_BUS.register(this);
    }

    private void commonSetup(final FMLCommonSetupEvent event) {
        // Some common setup code
        LOGGER.info("HELLO FROM COMMON SETUP");
    }


    private static void addOtherItemsToTab(CreativeModeTab.Output output, String thing) {
        List<RegistryObject<Item>> sortedItems = ItemRegistry.GENERATED_ITEMS.values().stream()
                .filter(itemRegistryObject -> itemRegistryObject.getId().getPath().matches(".*_" + thing))
                .sorted((o1, o2) -> {
                    String name1 = o1.getId().getPath();
                    String name2 = o2.getId().getPath();
                    return name1.compareTo(name2); // Sort by item name
                })
                .collect(Collectors.toList());

        for (RegistryObject<Item> item : sortedItems) {
            output.accept(item.get());
        }
    }

    private static void addItemsToTab(CreativeModeTab.Output output, String toolType) {
        List<RegistryObject<Item>> sortedItems = ItemRegistry.GENERATED_ITEMS.values().stream()
                .filter(itemRegistryObject -> itemRegistryObject.getId().getPath().matches(".*_" + toolType + "_.*"))
                .sorted((o1, o2) -> {
                    String name1 = o1.getId().getPath();
                    String name2 = o2.getId().getPath();
                    return name1.compareTo(name2); // Sort by item name
                })
                .collect(Collectors.toList());

        for (RegistryObject<Item> item : sortedItems) {
            output.accept(item.get());
        }
    }

    private static void addMiscItemsToTab(CreativeModeTab.Output output) {
        List<RegistryObject<Item>> sortedItems = ItemRegistry.GENERATED_ITEMS.values().stream()
                .filter(itemRegistryObject -> {
                    String itemPath = itemRegistryObject.getId().getPath();
                    return !itemPath.matches(".*_(sword|pickaxe|axe|shovel|hoe)_.*") && !itemPath.matches(".*_(bed|shield|torch)");
                })
                .sorted((o1, o2) -> {
                    String name1 = o1.getId().getPath();
                    String name2 = o2.getId().getPath();

                    // Get the last word (after the last underscore)
                    String lastWord1 = name1.substring(name1.lastIndexOf('_') + 1);
                    String lastWord2 = name2.substring(name2.lastIndexOf('_') + 1);

                    // Compare the last words first
                    int lastWordComparison = lastWord1.compareTo(lastWord2);
                    if (lastWordComparison != 0) {
                        return lastWordComparison;
                    }

                    // If last words are the same, compare the full names
                    return name1.compareTo(name2);
                })
                .collect(Collectors.toList());

        for (RegistryObject<Item> item : sortedItems) {
            output.accept(item.get());
        }
    }

}
