package one.fayaz.fariance.blocks;

import net.minecraft.world.entity.player.Player;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.tags.ItemTags;

import net.minecraftforge.event.entity.player.PlayerEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import one.fayaz.fariance.FarianceMod;

@Mod.EventBusSubscriber(modid = FarianceMod.MODID)  // Updated MOD_ID to MODID
public class CraftingEventHandler {

    @SubscribeEvent
    public static void onItemCrafted(PlayerEvent.ItemCraftedEvent event) {
        // Get the player who crafted the item
        Player player = event.getEntity();  // Use getEntity instead of getPlayer

        // Check if the crafted item is a pickaxe using the Pickaxes tag
        if (event.getCrafting().is(ItemTags.PICKAXES)) {
            // Only run the recipe unlock logic on the server side
            if (player instanceof ServerPlayer) {
                unlockPickaxeRecipesForPlayer((ServerPlayer) player);
            }
        }
    }

    private static void unlockPickaxeRecipesForPlayer(ServerPlayer player) {
        // Unlock every recipe if the result of the recipe is an item in the tag for pickaxes
    }
}
