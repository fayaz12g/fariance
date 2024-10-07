package one.fayaz.fariance.blocks;

import net.minecraft.core.BlockPos;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.InteractionResult;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.AxeItem;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.RotatedPillarBlock;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.block.state.StateDefinition;
import net.minecraft.world.phys.BlockHitResult;
import net.minecraftforge.registries.RegistryObject;
import one.fayaz.fariance.ItemRegistry;

public class CustomLogBlock extends RotatedPillarBlock {
    private String logName = "pale_oak_log";

    public CustomLogBlock(Properties properties, String logName) {
        super(properties);
        this.logName = logName; // Store the name of the log type
    }


    public InteractionResult use(Level level, BlockPos pos, BlockState state, ServerPlayer player,
                                 InteractionHand hand, BlockHitResult hit) {
        ItemStack itemStack = player.getItemInHand(hand);

        // Check if the item is an Axe
        if (itemStack.getItem() instanceof AxeItem) {
            // Replace the block with the stripped variant
            if (!level.isClientSide) {
                String strippedLogType = "stripped_" + this.logName; // Construct the stripped variant name

                // Get the stripped block's registry object
                RegistryObject<Block> strippedBlock = ItemRegistry.GENERATED_BLOCKS.get(strippedLogType);

                if (strippedBlock != null) {
                    level.setBlockAndUpdate(pos, strippedBlock.get().defaultBlockState()); // Set the block to its stripped variant
//                    itemStack.hurtAndBreak(1, player, (p) -> p.broadcastBreakEvent(hand)); // Damage the axe
                }
            }
            return InteractionResult.sidedSuccess(level.isClientSide);
        }

        return InteractionResult.PASS;
    }

    @Override
    protected void createBlockStateDefinition(StateDefinition.Builder<Block, BlockState> builder) {
        super.createBlockStateDefinition(builder);
    }
}
