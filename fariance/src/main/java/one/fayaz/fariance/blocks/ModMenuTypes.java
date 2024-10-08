package one.fayaz.fariance.blocks;

import net.minecraft.core.BlockPos;
import net.minecraft.world.Container;
import net.minecraft.world.inventory.MenuType;
import net.minecraft.world.level.Level;
import net.minecraftforge.common.extensions.IForgeMenuType;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;
import one.fayaz.fariance.FarianceMod;

public class ModMenuTypes {
    public static final DeferredRegister<MenuType<?>> MENUS = DeferredRegister.create(ForgeRegistries.MENU_TYPES, FarianceMod.MODID);

    public static final RegistryObject<MenuType<CustomBarrelMenu>> CUSTOM_BARREL_MENU =
            MENUS.register("custom_barrel", () -> IForgeMenuType.create((windowId, inv, data) -> {
                BlockPos pos = data.readBlockPos();
                Level level = inv.player.level();
                return new CustomBarrelMenu(windowId, inv, (Container)level.getBlockEntity(pos));
            }));

    // Don't forget to register MENUS with your mod event bus in your mod's constructor
    public static void register(IEventBus eventBus) {
        MENUS.register(eventBus);
    }
}
